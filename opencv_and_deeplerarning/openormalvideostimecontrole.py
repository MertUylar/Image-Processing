import cv2
import time

cap = cv2.VideoCapture('DATA/video_capture.mp4')

fps = 25

if cap.isOpened()== False: 
    print("Error ")
    

# While the video is opened
while cap.isOpened():
    
    
    
    # Read the video file.
    ret, frame = cap.read()
    
    # If we got frames, show them.
    if ret == True:
        
        
        

        
        time.sleep(1/fps)  #it controled time with using videous
        cv2.imshow('frame',frame)
 
        # Press q to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            
            break
 
 
    else:
        break
        
cap.release()
# Closes all the frames
cv2.destroyAllWindows()