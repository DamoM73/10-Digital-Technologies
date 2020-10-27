import time
import cv2
import numpy as np
from imutils.video import VideoStream
import imutils

# set inital frame size
frameSize = (320,240)

# initalize multithreading the video stream
vs = VideoStream(src=0, usePiCamera=True, resolution=frameSize, framerate=32).start()

# allow camera to warm up
time.sleep(2.0)

timeCheck = time.time()
while True:
    # get the next frame
    frame = vs.read()
    
    # show video stream
    cv2.imshow('orig',frame)
    key = cv2.waitKey(1) & 0xff
    
    # if the 'q' key was pressed, break from the loop
    if key == ord("q"):
        break
    
    print(1/(time.time() - timeCheck))
    timeCheck = time.time()
    
# cleanup before exit
cv2.destroyAllWindows()
vs.stop()