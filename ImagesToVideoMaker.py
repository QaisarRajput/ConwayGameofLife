# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 04:33:52 2020

@author: qasis
"""

import cv2
import os

image_folder = os.getcwd() + "\\Images"
video_name = os.getcwd() + "\\video.avi"

print(image_folder)
print(video_name)

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter(video_name, fourcc, 5, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()