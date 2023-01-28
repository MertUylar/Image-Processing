import cv2
import numpy as np 
import matplotlib.pyplot as plt


flat_chess=cv2.imread('DATA/flat_chessboard.png')

plt.imshow(flat_chess)

found,corners=cv2.findChessboardCorners(flat_chess,(7,7)) #found köşeleri bulup bulmadıgını söylüyor 


print(corners)

cv2.drawChessboardCorners(flat_chess,(7,7),corners,found)

plt.imshow(flat_chess)


dots=cv2.imread('DATA/dot_grid.png')

plt.imshow(dots)



found,corners=cv2.findChessboardCorners(dots,(10,10),cv2.CALIB_CB_SYMMETRIC_GRID) #found köşeleri bulup bulmadıgını söylüyor 

cv2.drawChessboardCorners(dots,(10,10),corners,found) #found köşeleri bulup bulmadıgını söylüyor 


plt.imshow(dots)