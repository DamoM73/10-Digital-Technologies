#import numpy as np
import cv2
import time
from imutils.video import VideoStream
#import imutils

frame_size = (320,240)

cap = VideoStream(src=0, usePiCamera=True, resolution=frame_size, framerate=32).start()

time.sleep(2.0)


while(True):
    frame = cap.read()
    
    frame = cv2.flip(frame, -1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
cv2.destroyAllWindows()
cap.stop()