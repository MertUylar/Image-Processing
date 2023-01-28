# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 15:56:35 2023

@author: Mert Eren
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

blank_img=np.zeros(shape=(512,512,3),dtype=np.int16)
print(blank_img.shape) #bunun dizi kısmını verir
plt.imshow(blank_img) #bunun gösterimini veriri

cv2.rectangle(blank_img,pt1=(50,100),pt2=(200,400),color=(0,255,0),thickness=-10)  #- olursa içi boyanmış olur 
plt.imshow(blank_img)  #burada turtle kütüphanesi ile yaptıgımız işlemin aynısını yaptık yeşil bir kare çizimi 


cv2.circle(img=blank_img,color=(255,0,0),thickness=10,radius=50,center=(100,100))
plt.imshow(blank_img)

cv2.line(blank_img,pt1=(0,0),pt2=(512,512),color=(102,255,255),thickness=2)   #line kısmı bildiğimi<
plt.imshow(blank_img)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img,text='hello',org=(10,500),fontFace=font,fontScale=4,color=(255,255,255),thickness=3,lineType=cv2.LINE_AA)
#org konum fontface tür scale boyut thickness kalılık

plt.imshow(blank_img)

blank_img=np.zeros(shape=(512,512,3),dtype=np.int32)
plt.imshow(blank_img)

vertices=np.array([[100,300],[200,200],[400,300],[200,400]],dtype=np.int32)

pts=vertices.reshape((-1,1,2))
print(vertices)
cv2.polylines(blank_img,[vertices],isClosed=True,color=(255,0,0),thickness=5) #pts yazsan da yiyor 
plt.imshow(blank_img)
