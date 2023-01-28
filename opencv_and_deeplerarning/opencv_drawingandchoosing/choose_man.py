import cv2
import numpy as np
# Create a function based on a CV2 Event (Left button click)

font=cv2.FONT_HERSHEY_SIMPLEX

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255),-1)
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),50,(0,255,0),2) ######geliştirmek için direk circle üstünde isim çımaya bakılmas gerekiyor
        cv2.putText(img,text='Name:Ted Villiam',org=(5,20),fontFace=font,fontScale=1,color=(255,0,255),thickness=1,lineType=cv2.LINE_AA)
        cv2.putText(img,text=' age:40',org=(5,40),fontFace=font,fontScale=1,color=(255,0,255),thickness=1,lineType=cv2.LINE_AA)

# Open Image
img = cv2.imread("ted.jpg")
# This names the window so we can reference it 
cv2.namedWindow(winname='dog')
# Connects the mouse button to our callback function
cv2.setMouseCallback('dog',draw_circle)

while True: #Runs forever until we break with Esc key on keyboard
    # Shows the image window
    cv2.imshow('dog',img)
    # EXPLANATION FOR THIS LINE OF CODE:
    # https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1/39201163
    if cv2.waitKey(20) & 0xFF == 27:
        break
# Once script is done, its usually good practice to call this line
# It closes all windows (just in case you have multiple windows called)
cv2.destroyAllWindows()
