# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:07:51 2023

@author: Mert Eren
"""

import cv2

img1=cv2.imread('DATA/dog_backpack.png')
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2=cv2.imread('DATA/watermark_no_copy.png')
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

import matplotlib.pyplot as plt



img2=cv2.resize(img2,(600,600))

plt.imshow(img1)
large_img=img1
small_image=img2

x_offset=0
y_offset=0
x_end=x_offset+small_image.shape[1]
y_end=y_offset+small_image.shape[0]

large_img[y_offset:y_end,x_offset:x_end]=small_image
plt.imshow(large_img)
#img1=cv2.resize(img1,(1200,1200)) #boyutunu ayarlamış olduk
#img2=cv2.resize(img2,(1200,1200))
#plt.imshow(img1)
#blended =cv2.addWeighted(src1=img1,alpha=0.7,src2=img2,beta=0.5,gamma=0)
#plt.imshow(blended) #blended yaptık bildiğimiz alpha saydamlık oranlarını veriyor

