import pandas as pd
import numpy as np
import cv2


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
