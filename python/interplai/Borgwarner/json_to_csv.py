import json
import os

import cv2
import pandas as pd

filename = []
width = []
height = []
Class = []
xmin = []
ymin = []
xmax = []
ymax = []
light_color = []
a = []
file_number = 0
# classes=['bus','light','traffic_sign','person','bike','truck','motor','car','train','Rider']
# classes=['bus','light','traffic light','person','bike','truck','motor','car','train','Rider',"traffic sign"]
classes = ['traffic light']
bblabel = []
loop = 0
jason_path="/home/mayank_s/saved_work/interplai/dataset/ann_arbor_ride_hailing_kepler.json"
# jason_path = "/home/mayank_s/codebase/cplus_plus/ai/darknet_AlexeyAB/coco/annotations/instances_val2014.json"
image_path = '/home/mayank_s/datasets/bdd/bdd100k_images/bdd100k/images/100k/val'

if 1:
    data = open(jason_path, 'r')
    data1 = data.read()
    data.close()
    Json = json.loads(data1)
    # filename.append(Json['name'])
    # for obj in root.iter('object'):
    # for ki in Json['frames'][0]['objects']:
    for ki in Json:
        loop += 1
        # print("count run", loop)
        # object_name=ki['category']
        file_name = ki['name']
        # ________________________________________________________________________
        Image_com_path = os.path.join(image_path, file_name)
        exists = os.path.isfile(Image_com_path)
        if exists:
            # if image_name.split('.')==k.split('.'):
            my_image = cv2.imread(Image_com_path, 1)
            # _______________________________________________________________________

            for dat_obj in ki['labels']:
                object_name = dat_obj['category']

                if ki['attributes']['timeofday'] == "daytime":
                    if object_name in classes:
                        light_color = ki['labels'][0]['attributes']['trafficLightColor']
                        xmin = int(dat_obj['box2d']['x1'])
                        xmax = int(dat_obj['box2d']['x2'])
                        ymin = int(dat_obj['box2d']['y1'])
                        ymax = int(dat_obj['box2d']['y2'])
                        width = my_image.shape[1]
                        height = my_image.shape[0]
                        # coordinate = [xmin, ymin, xmax, ymax, class_num]
                        # object_name=object_name+"_"+light_color
                        object_name = "traffic_light"
                        data_label = [file_name, width, height, object_name, xmin, ymin, xmax, ymax]
                        # data_label = [file_name, width, height, object_name, xmin, ymin, xmax, ymax]
                        if not ((xmin == xmax) and (ymin == ymax)):
                            bblabel.append(data_label)
                            print(file_name)
                            # print()
        else:
            print("file_name")
        # except IOError:
        #     print("error at loop:{lp} and image:{dt}".format(lp=loop,dt=dat))
        #     print('error1')
        # except:
        #     print("error at loop:{lp} and image:{dt}".format(lp=loop, dt=dat))
        #     print('error2')
        #     # print('ERROR...object detecion failed for Filename: {fn} , Check file type '.format(fn=filename), '\n')
        # else:
        #     print("successfull for ", dat)

columns = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']

# pd1=pd.DataFrame(a,columns=columns)
# df=pd.DataFrame(bblabel)
# df.to_csv('out.csv')
# pd1.to_csv('output_bb.csv')

df = pd.DataFrame(bblabel, columns=columns)
df.to_csv('BBD_daytime_val.csv')
