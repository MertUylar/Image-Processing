# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:17:04 2023

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


print(img1.shape)

x_offset=934-600
y_offset=1401-600

rows,cols,channels=img2.shape

roi=img1[y_offset:1401,x_offset:943]

plt.imshow(roi)

img2gray=cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
plt.imshow(img2gray,cmap='gray')

mask_inv=cv2.bitwise_not(img2gray) #tersine çevirme işlemi
plt.imshow(mask_inv,cmap='gray')

import numpy as np
white_background=np.full(img2.shape,255,dtype=np.uint8) #600 e600 shape değeri

bk=cv2.bitwise_or(white_background,white_background,mask=mask_inv)

fg=cv2.bitwise_or(img2,img2,mask=mask_inv)
plt.imshow(fg)

bk=cv2.bitwise_or(white_background,white_background,mask=mask_inv)
plt.imshow(bk)

final_roi=cv2.bitwise_or(roi,fg)
plt.imshow(final_roi)


large_img=img1
small_img=final_roi
large_img[y_offset:y_offset+small_img.shape[0],x_offset:x_offset+small_img.shape[1]]=small_img
plt.imshow(large_img)