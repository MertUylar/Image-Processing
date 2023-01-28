# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 15:02:22 2023

@author: Mert Eren
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('DATA/internal_external.png',0)
img.shape

plt.imshow(img,cmap="gray")


contours,hierarchy=cv2.findContours(img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
# Draw External Contours

# Set up empty array
external_contours = np.zeros(img.shape)

# For every entry in contours
for i in range(len(contours)):
    
    # last column in the array is -1 if an external contour (no contours inside of it)
    if hierarchy[0][i][3] == -1:
        
        # We can now draw the external contours from the list of contours
        cv2.drawContours(external_contours, contours, i, 255, -1)

plt.imshow(external_contours,cmap="gray")        
# Create empty array to hold internal contours
image_internal = np.zeros(img.shape)

# Iterate through list of contour arrays
for i in range(len(contours)):
    # If third column value is NOT equal to -1 than its internal
    if hierarchy[0][i][3] != -1:
        
        # Draw the Contour
        cv2.drawContours(image_internal, contours, i, 255, -1)
plt.imshow(image_internal,cmap="gray") 


