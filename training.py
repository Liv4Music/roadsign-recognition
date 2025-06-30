import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import uuid  
import os
import time

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
labels = ['speedSign']
number_imgs = 108

def train_speed_sign():
    os.system('cd yolov5')
    os.system('python train.py --img 320 --batch 16 --epochs 500 --data dataset.yml --weights yolov5s.pt --workers 2')
    os.system('cd ..')