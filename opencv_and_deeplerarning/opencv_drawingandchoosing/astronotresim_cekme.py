# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 18:15:35 2023

@author: Mert Eren
"""
import cv2

# içe aktarma
img = cv2.imread("ted.jpg", 0)  

# görselleştir
cv2.imshow("Tedin resmi", img)

k = cv2.waitKey(0) &0xFF

if k == ord('q'): # wsc   #q ya bastığı anda kapat eğer bu olmazsa çıkarken hata verir
    cv2.destroyAllWindows()
elif k == ord('s'):         # s ile fotoğraf görüntüsünü al ve kapat 
    cv2.imwrite("ilktedinfotosu.png", img)
    cv2.destroyAllWindows()  #görseli kapatma
    