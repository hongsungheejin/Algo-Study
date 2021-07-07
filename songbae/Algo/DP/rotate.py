import math 

def rotate(origin, point, angle):
  '''
  Rotate a point counterclockwise by a given angle around a given origin 
  The angle should be given in radians
  '''
  global test_img,img
  h,w=len(test_img), len(test_img[0])
  ox, oy  = origin 
  px,py =point 
  qx= ox+math.cos(angle)*(px-ox)-math.sin(angle)*(py-oy)
  qy=oy+math.sin(angle)*(px-ox)+math.cos(angle)*(py-oy)
  qx= round(qx)
  qy= round(qy)
  if qx<0 or qy <0 or qx>=h or qy>=w:return
  test_img[qx][qy][:]=img[px][py][:]
  return 

import matplotlib.pyplot as plt 
import math as m
import cv2 
import copy
import numpy as np 
img=cv2.imread('../../ong.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
test_img= np.zeros_like(img)
print(test_img.shape)
test_img=test_img.tolist()
h,w,c=img.shape
center=(h//2,w//2)

for H in range(h):
  for W in range(w):
    rotate(center,(H,W),m.radians(30))


img=np.array(img,dtype=np.uint8)
test_img=np.array(test_img,dtype=np.uint8)
cv2.imshow('image',img)
cv2.imshow('rotate_img',test_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
