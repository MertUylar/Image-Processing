
import cv2


# Connects to your computer's default camera
cap = cv2.VideoCapture(0)


# Automatically grab width and height from video feed
# (returns float which we need to convert to integer for later on!)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


writer=cv2.VideoWriter('mysupervideo.mp4',cv2.VideoWriter_fourcc(*'DIVX'),20,(width,height)) #pwd nereye kaydedilecegini gösterir
while True:
    
    
    ret, frame = cap.read()

    #drawing
    writer.write(frame)
   # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   
    cv2.imshow('frame',frame)
    
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
writer.release()
cap.release()
cv2.destroyAllWindows()  