# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 09:23:45 2023

@author: Mert Eren
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


################################
full=cv2.imread('DATA/sammy.jpg')
full =cv2.cvtColor(full,cv2.COLOR_BGR2RGB)
plt.imshow(full)
##################################

face=cv2.imread('DATA/sammy_face.jpg')
face=cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
plt.imshow(face)
print(face.shape)

# All the 6 methods for comparison in a list
# Note how we are using strings, later on we'll use the eval() function to convert to function
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for m in methods:
    
    full_copy=full.copy()
    method=eval(m )  #sayı olmayan şeyleri karşılaştırmada kullanuluyor 
    
    #template matching
    
    res=cv2.matchTemplate(full_copy,face,method) 
    
    
    my_method= eval('cv2.TM_CCOEFF')
    res=cv2.matchTemplate(full_copy,face,my_method)
    plt.imshow(res)
    