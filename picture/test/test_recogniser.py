# Copyright 2018 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# !/usr/bin/python3
import time
import unittest
from unittest.mock import Mock
import argparse
from sensor_msgs.msg import Image
import numpy as np
import builtin_interfaces.msg
import rclpy
import rectifier.recogniser
from std_msgs.msg import String
from traffic_light_msgs.msg import TrafficLightStruct
from cv_bridge import CvBridge
import cv2

class TestTimeSource(unittest.TestCase):
    def setUp(self):
        rclpy.init(args=None)
        ####################################################333333
        parser = argparse.ArgumentParser()
        parser.add_argument('--cfg', type=str, default='/module/src/rectifier/rectifier/cfg/yolov3.cfg', help='*.cfg path')
        parser.add_argument('--names', type=str, default='data/coco.names', help='*.names path')
        parser.add_argument('--weights', type=str, default='/module/src/rectifier/rectifier/weights/color_model.pt',
                            help='weights path')
        parser.add_argument('--source', type=str, default='data/samples', help='source')
        parser.add_argument('--output', type=str, default='output', help='output folder')  # output folder
        parser.add_argument('--img-size', type=int, default=416, help='inference size (pixels)')
        parser.add_argument('--conf-thres', type=float, default=0.3, help='object confidence threshold')
        parser.add_argument('--iou-thres', type=float, default=0.6, help='IOU threshold for NMS')
        parser.add_argument('--fourcc', type=str, default='mp4v', help='output video codec (verify ffmpeg support)')
        parser.add_argument('--half', action='store_true', help='half precision FP16 inference')
        parser.add_argument('--device', default='0', help='device id (i.e. 0 or 0,1) or cpu')
        parser.add_argument('--view-img', default=False,action='store_true', help='display results')
        parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
        parser.add_argument('--classes', nargs='+', type=int, help='filter by class')
        parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
        opt = parser.parse_args()
        self.myobject =  rectifier.recogniser.Recogniser(opt)


    def tearDown(self):
        self.myobject.destroy_node()
        rclpy.shutdown()

    def test_rectifeir(self):
        cv_image=cv2.imread("/module/src/rectifier/test/test_image.jpg",1)
        bridge = CvBridge()
        image_message = bridge.cv2_to_imgmsg(cv_image, encoding="bgr8") 
        # image_message.encoding="bayer_rggb8"
        mydata=TrafficLightStruct()
        mydata.raw_image=image_message
        mydata.selected_box.x_offset=1117
        mydata.selected_box.y_offset=403
        mydata.selected_box.height=106
        mydata.selected_box.width=50
        self.assertIsNotNone(self.myobject.img_callback(mydata))   

        

if __name__ == '__main__':
    unittest.main()
