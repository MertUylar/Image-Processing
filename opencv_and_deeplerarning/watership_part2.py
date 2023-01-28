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
##############################################ayrı ayrı hesaplama
img=cv2.imread('DATA/pennies.jpg')
img=cv2.medianBlur(img,35)
display(img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
display(thresh)
###################
# NOİSE REMOVAL İSTEYE BAĞLIDIR
kernel=np.ones((3,3),np.uint8)
opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)
sure_bg = cv2.dilate(opening,kernel,iterations=3)
display(sure_bg,cmap='gray')
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0) ##mesafe dönüşümü yaptık
display(dist_transform)

display(sure_fg)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
display(unknown)
ret, markers = cv2.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1
# Now, mark the region of unknown with zero
markers[unknown==255] = 0
markers = cv2.watershed(img,markers)
display(markers)

contours, hierarchy = cv2.findContours(markers.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
#EN SONDA TOHUMLARI ÇERÇEVELİYORUZ
# For every entry in contours
for i in range(len(contours)):
    
    # last column in the array is -1 if an external contour (no contours inside of it)
    if hierarchy[0][i][3] == -1:
        
        # We can now draw the external contours from the list of contours
        cv2.drawContours(sep_coins, contours, i, (255, 0, 0), 10)
        
display(sep_coins)        