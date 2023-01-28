# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 00:39:53 2023

@author: Mert Eren
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt


def display(img,cmap=None):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap=cmap)
    
    
sep_coins=cv2.imread('DATA/pennies.jpg')  

display(sep_coins)

#median blur
#graycale
#binary threshold
#find contour

sep_blur=cv2.medianBlur(sep_coins,25)
display(sep_blur)
gray_sep_coins=cv2.cvtColor(sep_blur,cv2.COLOR_BGR2GRAY)
display(gray_sep_coins)

ret,sep_thresh=cv2.threshold(gray_sep_coins,180,255,cv2.THRESH_BINARY_INV)

display(sep_thresh)

contours,hierarchy=cv2.findContours(sep_thresh.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    if hierarchy[0][i][3]==-1:
        cv2.drawContours(sep_coins,contours,i,(255,0,0),10)
        
display(sep_coins)        
