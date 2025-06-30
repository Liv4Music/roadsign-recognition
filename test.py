import torch
import numpy as np
import cv2
import uuid  
import os
import time
import torch
import matplotlib.pyplot as plt
import cv2

def test_img():

    # Load the model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp/weights/last.pt', force_reload=True)

    # Load and predict on image
    img_path = '/Users/liv/Documents/Personal/RoadSign/roadsign-recognition/data/test/test1.jpeg'
    results = model(img_path)

    # Render image with bounding boxes (as list of np arrays in BGR)
    rendered_img_bgr = results.render()[0]

    # Convert BGR to RGB for matplotlib
    rendered_img_rgb = cv2.cvtColor(rendered_img_bgr, cv2.COLOR_BGR2RGB)

    # Show using matplotlib
    plt.imshow(rendered_img_rgb)
    plt.pause(0.001)
    plt.axis('off')
    plt.show()

    cv2.imwrite("output_with_boxes.jpg", rendered_img_bgr)