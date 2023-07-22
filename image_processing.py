#pip install opencv-contrib-python

import cv2
import numpy as np

#read image
plane=r'C:\Users\chand\Desktop\airplane.jpeg'
img=cv2.imread(plane)
if img is None:
  print('Could not find or open the image:',plane)
  exit(0)
print('type',type(img))
print('shape',img.shape)

#resize the image by width and height
img_200=cv2.resize(img, (250,170))

#resize the image by scale
img_25pct=cv2.resize(img, (0,0),fx=0.25,fy=0.25)

#filters-grey scale,egde detection,bgrtorgb
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_edge=cv2.Canny(img,500,100) #100,200 are threshold values

#display image
cv2.imshow('image gray',img_gray)
cv2.imshow('image rgb',img_rgb)
cv2.imshow('image',img)
cv2.imshow('image edge',img_edge)
cv2.waitKey(0) #holds until the key is pressed