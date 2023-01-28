# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:26:31 2023

@author: Mert Eren
"""
# amaç sol ve sağ clicklere basıp bir obje çıkarma 
import cv2
import numpy as np
img=np.zeros((512,512,3),np.int8)

def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),-1) #100:dairenin yarçapı diğeri rengi diğeri de içini boyamak
    elif event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(200,2,0),-1) 
        
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_circle)


while True:
    
    
    cv2.imshow('my_drawing',img)
    if cv2.waitKey(20)& 0xFF==27:
        break
    
cv2.destroyAllWindows()    