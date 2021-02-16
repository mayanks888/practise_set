import numpy as np
import cv2
from pathlib import Path
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torchvision import models, transforms, utils
import copy
from oneshot.utils import *
from PIL import Image

class ImageDataset(torch.utils.data.Dataset):
    def __init__(self, template_dir_path, image_name, thresh_csv=None, transform=None):
        self.transform = transform
        if not self.transform:
            self.transform = transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406],
                    std=[0.229, 0.224, 0.225],
                )
            ])
        self.template_path = list(template_dir_path.iterdir())
        self.image_name = image_name
        self.image_raw = cv2.imread(self.image_name)
        height, width, channels = self.image_raw.shape
        self.scale_resize = 2
        self.image_raw=cv2.resize(self.image_raw,(int(self.image_raw.shape[1]/self.scale_resize),int(self.image_raw.shape[0]/self.scale_resize)))
        self.thresh_df = None
        if thresh_csv:
            self.thresh_df = pd.read_csv(thresh_csv)
        if self.transform:
            self.image = self.transform(self.image_raw).unsqueeze(0)

    def __len__(self):
        return len(self.template_names)

    def __getitem__(self, idx):
        template_path = str(self.template_path[idx])
        template = cv2.imread(template_path)
        template=cv2.resize(template,(int(template.shape[1]/self.scale_resize),int(template.shape[0]/self.scale_resize)))

        if self.transform:
            template = self.transform(template)
        thresh = 0.7
        # thresh = .99
        if self.thresh_df is not None:
            if self.thresh_df.path.isin([template_path]).sum() > 0:
                thresh = float(self.thresh_df[self.thresh_df.path == template_path].thresh)
        return {'image': self.image,
                'image_raw': self.image_raw,
                'image_name': self.image_name,
                'template': template.unsqueeze(0),
                'template_name': template_path,
                'template_h': template.size()[-2],
                'template_w': template.size()[-1],
                'thresh': thresh}

# ### EXTRACT FEATURE

class Featex():
    def __init__(self, model, use_cuda):
        self.use_cuda = use_cuda
        self.feature1 = None
        self.feature2 = None
        self.model= copy.deepcopy(model.eval())
        self.model = self.model[:17]

        for param in self.model.parameters():
            param.requires_grad = False
        if self.use_cuda:
            self.model = self.model.cuda()
        self.model[2].register_forward_hook(self.save_feature1)
        self.model[16].register_forward_hook(self.save_feature2)
        self.col_model = self.model[:8]
        self.fc1 = nn.Linear(15 * 15 * 128, 1000)
        self.fc2 = nn.Linear(1000, 64)
        self.fc3 = nn.Linear(64, 4)
        self.col_seq=nn.Sequential(
            self.col_model,
            nn.Linear(15 * 15 * 128, 1000),
            nn.Linear(1000, 64),
            nn.Linear(64, 4))

    def save_feature1(self, module, input, output):
        self.feature1 = output.detach()
    
    def save_feature2(self, module, input, output):
        self.feature2 = output.detach()
        
    def __call__(self, input, mode='big'):
        if self.use_cuda:
            input = input.cuda()
        _ = self.model(input)
        if mode=='big':
            self.feature1 = F.interpolate(self.feature1, size=(self.feature2.size()[2], self.feature2.size()[3]), mode='bilinear', align_corners=True)
        else:        
            self.feature2 = F.interpolate(self.feature2, size=(self.feature1.size()[2], self.feature1.size()[3]), mode='bilinear', align_corners=True)
        return torch.cat((self.feature1, self.feature2), dim=1)



class MyNormLayer():
    def __call__(self, x1, x2):
        bs, _ , H, W = x1.size()
        _, _, h, w = x2.size()
        x1 = x1.view(bs, -1, H*W)
        x2 = x2.view(bs, -1, h*w)
        concat = torch.cat((x1, x2), dim=2)
        x_mean = torch.mean(concat, dim=2, keepdim=True)
        x_std = torch.std(concat, dim=2, keepdim=True)
        x1 = (x1 - x_mean) / x_std
        x2 = (x2 - x_mean) / x_std
        x1 = x1.view(bs, -1, H, W)
        x2 = x2.view(bs, -1, h, w)
        return [x1, x2]


class CreateModel():
    def __init__(self, alpha, model, use_cuda):
        self.alpha = alpha
        self.featex = Featex(model, use_cuda)
        self.I_feat = None
        self.I_feat_name = None
    def __call__(self, template, image, image_name):
        T_feat = self.featex(template)
        if self.I_feat_name is not image_name:
            self.I_feat = self.featex(image)
            self.I_feat_name = image_name
        conf_maps = None
        batchsize_T = T_feat.size()[0]
        for i in range(batchsize_T):
            T_feat_i = T_feat[i].unsqueeze(0)
            I_feat_norm, T_feat_i = MyNormLayer()(self.I_feat, T_feat_i)
            dist = torch.einsum("xcab,xcde->xabde", I_feat_norm / torch.norm(I_feat_norm, dim=1, keepdim=True), T_feat_i / torch.norm(T_feat_i, dim=1, keepdim=True))
            conf_map = QATM(self.alpha)(dist)
            if conf_maps is None:
                conf_maps = conf_map
            else:
                conf_maps = torch.cat([conf_maps, conf_map], dim=0)
        return conf_maps


class QATM():
    def __init__(self, alpha):
        self.alpha = alpha
    def __call__(self, x):
        batch_size, ref_row, ref_col, qry_row, qry_col = x.size()
        x = x.view(batch_size, ref_row*ref_col, qry_row*qry_col)
        xm_ref = x - torch.max(x, dim=1, keepdim=True)[0]
        xm_qry = x - torch.max(x, dim=2, keepdim=True)[0]
        confidence = torch.sqrt(F.softmax(self.alpha*xm_ref, dim=1) * F.softmax(self.alpha * xm_qry, dim=2))
        conf_values, ind3 = torch.topk(confidence, 1)
        ind1, ind2 = torch.meshgrid(torch.arange(batch_size), torch.arange(ref_row*ref_col))
        ind1 = ind1.flatten()
        ind2 = ind2.flatten()
        ind3 = ind3.flatten()
        if x.is_cuda:
            ind1 = ind1.cuda()
            ind2 = ind2.cuda()
        values = confidence[ind1, ind2, ind3]
        values = torch.reshape(values, [batch_size, ref_row, ref_col, 1])
        return values
    
    def compute_output_shape( self, input_shape ):
        bs, H, W, _, _ = input_shape
        return (bs, H, W, 1)


# # NMS AND PLOT
# ## SINGLE
def nms(score, w_ini, h_ini, thresh=0.7):
    score=score.squeeze()
    dots = np.array(np.where(score > thresh*score.max()))
    x1 = dots[1] - w_ini//2
    x2 = x1 + w_ini
    y1 = dots[0] - h_ini//2
    y2 = y1 + h_ini
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    scores = score[dots[0], dots[1]]
    order = scores.argsort()[::-1]
    if order.size > 0:
        max_score = scores[order[0]]
    else:
        max_score=0
    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])
        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h
        ovr = inter / (areas[i] + areas[order[1:]] - inter)
        inds = np.where(ovr <= 0.8)[0]
        order = order[inds + 1]
    boxes = np.array([[x1[keep], y1[keep]], [x2[keep], y2[keep]]]).transpose(2, 0, 1)
    scores=scores[keep]
    return boxes,scores,max_score


def plot_result(image_raw, boxes, show=False, save_name=None, color=(0, 0, 255)):
    # plot result
    d_img = image_raw.copy()
    for i,box in enumerate(boxes):
        bbox_info = boxes[i][None, :, :].copy()
        xmin = bbox_info[0, 0][0]
        xmax = bbox_info[0, 1][0]
        ymin = bbox_info[0, 0][1]
        ymax = bbox_info[0, 1][1]
        print('boxes info ',xmin, ymin,xmax,ymax,d_img.shape)
        d_img = cv2.rectangle(d_img, tuple(box[0]), tuple(box[1]), color, 2)
    show=True
    if show:
        cv2.namedWindow('one_shot_Detection',cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('one_shot_Detection', 400,400)
        cv2.moveWindow('one_shot_Detection', 1400,500) 
        cv2.imshow("one_shot_Detection", d_img)
        ch = cv2.waitKey(1)
    if save_name:
        cv2.imwrite(save_name, d_img[:,:,::-1])
    return d_img


def run_one_sample(model, dataset):
    for data in dataset:
        template=data['template']
        image=  data['image']
        image_name= data['image_name']
        w_array=(data['template_w'])
        h_array=(data['template_h'])
        thresh_list=(data['thresh'])
    val = model(template, image, image_name)
    if val.is_cuda:
        val = val.cpu()
    val = val.numpy()
    val = np.log(val)

    batch_size = val.shape[0]
    scores = []
    for i in range(batch_size):
        # compute geometry average on score map
        gray = val[i, :, :, 0]
        gray = cv2.resize(gray, (image.size()[-1], image.size()[-2]))
        h = template.size()[-2]
        w = template.size()[-1]
        score = compute_score(gray, w, h)
        score[score > -1e-7] = score.min()
        score = np.exp(score / (h * w))  # reverse number range back after computing geometry average
        scores.append(score)
    return np.array(scores),np.array(w_array), np.array(h_array), thresh_list



