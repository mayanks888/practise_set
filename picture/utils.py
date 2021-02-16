from __future__ import print_function, division
import math
import numpy as np
import os, sys
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
# from oneshot.utils import *
from PIL import Image


int_ = lambda x: int(round(x))

def IoU( r1, r2 ):
    x11, y11, w1, h1 = r1
    x21, y21, w2, h2 = r2
    x12 = x11 + w1; y12 = y11 + h1
    x22 = x21 + w2; y22 = y21 + h2
    x_overlap = max(0, min(x12,x22) - max(x11,x21) )
    y_overlap = max(0, min(y12,y22) - max(y11,y21) )
    I = 1. * x_overlap * y_overlap
    U = (y12-y11)*(x12-x11) + (y22-y21)*(x22-x21) - I
    J = I/U
    return J


def evaluate_iou( rect_gt, rect_pred ):
    # score of iou
    score = [ IoU(i, j) for i, j in zip(rect_gt, rect_pred) ]
    return score


def compute_score( x, w, h ):
    # score of response strength
    k = np.ones( (h, w) )
    score = cv2.filter2D(x, -1, k)
    score[:, :w//2] = 0
    score[:, math.ceil(-w/2):] = 0
    score[:h//2, :] = 0
    score[math.ceil(-h/2):, :] = 0
    return score


def locate_bbox( a, w, h ):
    row = np.argmax( np.max(a, axis=1) )
    col = np.argmax( np.max(a, axis=0) )
    x = col - 1. * w / 2
    y = row - 1. * h / 2
    return x, y, w, h


def score2curve( score, thres_delta = 0.01 ):
    thres = np.linspace( 0, 1, int(1./thres_delta)+1 )
    success_num = []
    for th in thres:
        success_num.append( np.sum(score >= (th+1e-6)) )
    success_rate = np.array(success_num) / len(score)
    return thres, success_rate


def all_sample_iou( score_list, gt_list):
    num_samples = len(score_list)
    iou_list = []
    for idx in range(num_samples):
        score, image_gt = score_list[idx], gt_list[idx]
        w, h = image_gt[2:]
        pred_rect = locate_bbox( score, w, h )
        iou = IoU( image_gt, pred_rect )
        iou_list.append( iou )
    return iou_list


def plot_success_curve( iou_score, title='' ):
    thres, success_rate = score2curve( iou_score, thres_delta = 0.05 )
    auc_ = np.mean( success_rate[:-1] )
    plt.figure()
    plt.grid(True)
    plt.xticks(np.linspace(0,1,11))
    plt.yticks(np.linspace(0,1,11))
    plt.ylim(0, 1)
    plt.title(title + 'auc={}'.format(auc_))
    plt.plot( thres, success_rate )
    plt.show()
    



def find_template(ref_id,ref_pos, df=""):
    mygroup = df.groupby(['obj_id'], sort=True)
    mydata = mygroup.groups
    concerned_list = mydata[ref_id].values
    data = df.values[concerned_list]
    # calculating eucldean distance
    x_dif = abs(data[:, 10] - ref_pos[0])
    y_dif = abs(data[:, 11] - ref_pos[1])
    total_dif = x_dif + y_dif

    min_dist_val=np.amin(total_dif)
    index = np.argmin(total_dif)
    min_x_dist =x_dif[index]
    min_y_dist =y_dif[index]
    img_name = data[index][0]
    bbox = data[index][5:9]

    if ((min_x_dist <2000 or min_y_dist <2000) and min_dist_val < 10000):
        return (img_name, bbox, min_dist_val)
    else:
          return 1, 1,1
    

def  increase_bounding_box_scale(img,mybbox,scale_width,scale_height):
    bbox_info=mybbox
    height, width, depth = img.shape
    centr_box = (int((bbox_info[0] + bbox_info[2])/2),int((bbox_info[1] + bbox_info[3])/2))
    temp_width=   bbox_info[2] - bbox_info[0]
    temp_height= bbox_info[3] - bbox_info[1]

    bbox_info[1]=int(bbox_info[1]-(scale_height*(temp_height/2)))
    bbox_info[3]=int(bbox_info[3]+(scale_height*(temp_height/2)))

    bbox_info[0]=int(bbox_info[0]-(scale_width*(temp_width/2)))
    bbox_info[2]=int(bbox_info[2]+(scale_width*(temp_width/2)))

    temp_width = bbox_info[2] - bbox_info[0]
    temp_height = bbox_info[3] - bbox_info[1]

    if bbox_info[1] < 0:
        bbox_info[3]=bbox_info[3]-abs(bbox_info[1])
        bbox_info[1] = 0

    if bbox_info[3]>height:
        bbox_info[1]=bbox_info[1]+abs(bbox_info[1]-height)
        bbox_info[3]=height

    if bbox_info[0] < 0:
        bbox_info[2] = bbox_info[2] - abs(bbox_info[0])
        bbox_info[0] = 0

    if bbox_info[2] > width:
        bbox_info[0] = bbox_info[0] + abs(bbox_info[2] - width)
        bbox_info[2] = width
    return bbox_info
