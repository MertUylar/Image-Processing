# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 11:41:50 2023

@author: Mert Eren
"""

import cv2 
import numpy as  np
 #variables
 #true whike button down,false while mouse button UP 
drawing=False
ix=-1
iy=-1
def draw_rectangle(event,x,y,flags,params):
    global ix,iy,drawing 
    
    if event== cv2.EVENT_LBUTTONDOWN:
        drawing =True
        ix,iy=x,y
        
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
              cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
    elif event==cv2.EVENT_LBUTTONDOWN:
        drawing=False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)     
# black
img=np.zeros((512,512,3))

cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing',draw_rectangle)

while True:
    cv2.imshow('my_drawing',img)
    
    
    #checks for esc
    if cv2.waitKey(1) & 0xFF==27:
        break
cv2.destroyAllWindows()      
