import cv2
import time
from imutils.video import VideoStream

# set variables
frame_size = (320,240)

# connect to camera
capture = VideoStream(src=0, usePiCamera=True, resolution=frame_size, framerate=32).start()

# allow camera to warm up
time.sleep(0.5)

# intiate main program loop
while(True):
    # grab an image of current frame from the camera
    frame = capture.read()
    
    # flip image so it's not upside down
    frame = cv2.flip(frame, -1)
    
    # create a monochrome image from original image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # display origianl image and gray image
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    
    # listen for exit key (q) to eixt main loop
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# close displayed images
cv2.destroyAllWindows()

# release camera
capture.stop()