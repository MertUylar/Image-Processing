# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:38:57 2023

@author: Mert Eren
"""

import cv2
import matplotlib.pyplot as plt
img=cv2.imread('DATA/rainbow.jpg',0)
plt.imshow(img,cmap='gray')

ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

plt.imshow(thresh1,cmap='gray')



img=cv2.imread('DATA/crossword.jpg',0)

plt.imshow(img,cmap='gray')


def show_pic(img):
    fig=plt.figure(figsize=(15,15))
    ax=fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    

ret,th1=cv2.threshold(img,200,255,cv2.THRESH_BINARY)    #sayıları arttırdıkca eşik değerini arttırmıs olursun deneme yanılma yoluyla yapabilirsin
show_pic(th1)


the2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)  #bura ile oynanması gerekiyor taş tespiti projesinde kullanılabilinir

show_pic(the2)


blended=cv2.addWeighted(src1=th1,alpha=0.6,src2=the2,beta=0.4,gamma=0) #iki şekli birleştirme

show_pic(blended)

