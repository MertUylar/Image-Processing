# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 20:36:25 2023

@author: Mert Eren
"""

import cv2
import numpy as np 
import matplotlib.pyplot as plt

img=cv2.imread('DATA/internal_external.png',0)

img.shape

plt.imshow(img,cmap='gray')


image,countours,gierarchy=cv2.findContours(img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)