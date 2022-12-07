#/usr/bin/env python
# -*- coding: UTF-8 -*-

import rosbag
import cv2
from cv_bridge import CvBridge
import csv
import logging

def logset():
    logging.basicConfig(level=logging.DEBUG,
                filename='new.log',
                filemode='a',
                format=
                '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                )

def readRgb(bag_file):
    bag = rosbag.Bag(bag_file, "r")
    bridge = CvBridge()
    bag_data = bag.read_messages('/k01/rgb/image_rect/compressed')
    for topic, msg, t in bag_data:
        cv_image = bridge.compressed_imgmsg_to_cv2(msg, "bgr8")
        cv2.imshow("Image window", cv_image)
        cv2.waitKey(3)
        
    bag.close()

def readKinectPos(bag_file):
    """_summary_

    Args:
        bag_file (fileAddress): an address of the bag file
    
    Description:
        读取rosbag包里面的Kienct骨骼点空间位置坐标
    """
    bag = rosbag.Bag(bag_file, "r")
    bag_data = bag.read_messages('/k01/body_tracking_data')
    with open(bag_file.split('.')[0]+'KinectPos.csv', mode='w') as data_file:
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        KinectJointName = ['Pelvis','SpineNaval','SpineChest','Neck',
                           'ClavicleLeft','ShoulderLeft','ElbowLeft','WristLeft','HandLeft','HandTipLeft','ThumbLeft',
                           'ClavicleRight','ShoulderRight','ElbowRight','WristRight','HandRight','HandTipRight','ThumbRight',
                           'HipLeft','KneeLeft','AnkleLeft','FootLeft',
                           'HipRight','KneeRight','AnkleRight','FootRight',
                           'Head','Nose','EyeLeft','EarLeft','EyeRight','EarRight'
                           ]
        row = ['time']
        for i in range(32):
            row.append(KinectJointName[i] + 'PosX')
            row.append(KinectJointName[i] + 'PosY')
            row.append(KinectJointName[i] + 'PosZ')
        data_writer.writerow(row)
        
        # Get all message on the /joint states topic
        for topic, msg, t in bag_data:
            
            m = msg.markers
            if m != []:
                row = [m[0].header.stamp.secs*1000000000 + m[0].header.stamp.nsecs]
                for i in range(32):
                    row.append(m[i].pose.position.x)
                    row.append(m[i].pose.position.y)
                    row.append(m[i].pose.position.z)
                data_writer.writerow(row)
            else:
                row = [0]
                for i in range(32):
                    row.append(0)
                    row.append(0)
                    row.append(0)
                data_writer.writerow(row)
                

    bag.close()

def readKinectQuat(bag_file):
    """_summary_

    Args:
        bag_file (fileAddress): an address of the bag file
    
    Description:
        读取rosbag包里面的Kienct骨骼点空间位置四元数表示
    """
    bag = rosbag.Bag(bag_file, "r")
    bag_data = bag.read_messages('/k01/body_tracking_data')
    with open(bag_file.split('.')[0]+'KinectQuat.csv', mode='w') as data_file:
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        KinectJointName = ['Pelvis','SpineNaval','SpineChest','Neck',
                           'ClavicleLeft','ShoulderLeft','ElbowLeft','WristLeft','HandLeft','HandTipLeft','ThumbLeft',
                           'ClavicleRight','ShoulderRight','ElbowRight','WristRight','HandRight','HandTipRight','ThumbRight',
                           'HipLeft','KneeLeft','AnkleLeft','FootLeft',
                           'HipRight','KneeRight','AnkleRight','FootRight',
                           'Head','Nose','EyeLeft','EarLeft','EyeRight','EarRight'
                           ]
        row = ['time']
        for i in range(32):
            row.append(KinectJointName[i] + 'QuatX')
            row.append(KinectJointName[i] + 'QuatY')
            row.append(KinectJointName[i] + 'QuatZ')
            row.append(KinectJointName[i] + 'QuatW')
        data_writer.writerow(row)
        
        # Get all message on the /joint states topic
        for topic, msg, t in bag_data:
            
            m = msg.markers
            if m != []:
                row = [m[0].header.stamp.secs*1000000000 + m[0].header.stamp.nsecs]
                for i in range(32):
                    row.append(m[i].pose.orientation.x)
                    row.append(m[i].pose.orientation.y)
                    row.append(m[i].pose.orientation.z)
                    row.append(m[i].pose.orientation.w)
                data_writer.writerow(row)
            else:
                row = [0]
                for i in range(32):
                    row.append(0)
                    row.append(0)
                    row.append(0)
                data_writer.writerow(row)
                

    bag.close()

if __name__ == "__main__":
    
    logset()
    bag_file = 'sbj01_bend1.bag'
    
    # readRgb(bag_file)
    readKinectPos(bag_file)
    readKinectQuat(bag_file)
    
# [   'time', 
        #     'PelvisPosX', 'PelvisPosY','PelvisPosZ',
        #     'SpineNavalPosX', 'SpineNavalPosY','SpineNavalPosZ',
        #     'SpineChestPosX', 'SpineChestPosY','SpineChestPosZ',
        #     'NeckPosX', 'NeckPosY','NeckPosZ',
        #     'ClavicleLeftPosX', 'ClavicleLeftPosY','ClavicleLeftPosZ',
        #     'ShoulderLeftPosX', 'ShoulderLeftPosY','ShoulderLeftPosZ',
        #     'ElbowLeftPosX', 'ElbowLeftPosY','ElbowLeftPosZ',
        #     'WristLeftPosX', 'WristLeftPosY','WristLeftPosZ',
        #     'HandLeftPosX', 'HandLeftPosY','HandLeftPosZ',
        #     'HandTipLeftPosX', 'HandTipLeftPosY','HandTipLeftPosZ',
        #     'ThumbLeftPosX', 'ThumbLeftPosY','ThumbLeftPosZ',
        #     'ClavicleRightPosX', 'ClavicleRightPosY','ClavicleRightPosZ',
        #     'ShoulderRightPosX', 'ShoulderRightPosY','ShoulderRightPosZ',
        #     'ElbowRightPosX', 'ElbowRightPosY','ElbowRightPosZ',
        #     'WristRightPosX', 'WristRightPosY','WristRightPosZ',
        #     'HandRightPosX', 'HandRightPosY','HandRightPosZ',
        #     'HandTipRightPosX', 'HandTipRightPosY','HandTipRightPosZ',
        #     'ThumbRightPosX', 'ThumbRightPosY','ThumbRightPosZ',
        #     'HipLeftPosX', 'HipLeftPosY','HipLeftPosZ',
        #     'KneeLeftPosX', 'KneeLeftPosY','KneeLeftPosZ',
        #     'AnkleLeftPosX', 'AnkleLeftPosY','AnkleLeftPosZ',
        #     'FootLeftPosX', 'FootLeftPosY','FootLeftPosZ',
        #     'HipRightPosX', 'HipRightPosY','HipRightPosZ',
        #     'KneeRightPosX', 'KneeRightPosY','KneeRightPosZ',
        #     'AnkleRightPosX', 'AnkleRightPosY','AnkleRightPosZ',
        #     'FootRightPosX', 'FootRightPosY','FootRightPosZ',
        #     'HeadPosX', 'HeadPosY','HeadPosZ',
        #     'NosePosX', 'NosePosY','NosePosZ',
        #     'EyeLeftPosX', 'EyeLeftPosY','EyeLeftPosZ',
        #     'EarLeftPosX', 'EarLeftPosY','EarLeftPosZ',
        #     'EyeRightPosX', 'EyeRightPosY','EyeRightPosZ',
        #     'EarRightPosX', 'EarRightPosY','EarRightPosZ',
        # ]