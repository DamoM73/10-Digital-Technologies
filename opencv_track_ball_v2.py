# import necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

# construct the arguement parse and parse the arguements
ap = argparse.ArgumentParser()
#ap.add_argument('-v', '--video', help='path to the (optional) video file')
args = vars(ap.parse_args())
buffer = 64

# define the lower and upper boundaries of the ball in the HSV color space
# initialize the lsit of tracked points
blue_lower = (89,138,50)
blue_upper = (125,255,164)
pts = deque(maxlen=buffer)

# grab the reference to the webcam
vs = VideoStream(src=0, usePiCamera=True).start()
    
# allow the camera or video file to intialise
time.sleep(0.5)

# main loop
while True:
    # grab the current frame
    frame = vs.read()
    
    # handle the frame from VideoCapture or Video Stream
    #frame = frame[1] if args.get("video", False) else frame
    
    # resize the frame, blur it flip it, and convert it to the HSV color space
    frame = cv2.flip(frame, -1)
    frame = imutils.resize(frame, width=1200)
    blurred = cv2.GaussianBlur(frame, (11,11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    # construct a mask for the color 'blue', then perform a series of dilations and erosions
    # to remove any small blobs left in the mask
    mask = cv2.inRange(hsv, blue_lower, blue_upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    # find the contours in the mask and initialize the current (x,y) center of the ball
    cents = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cents = imutils.grab_contours(cents)
    center = None
    
    # only proceed if at least one contour was found
    if len(cents) > 0:
        # find the largest contour in the mask,then use it to compute 
        # the minimum enclosing circle and centroid
        c = max(cents, key=cv2.contourArea)
        ((x,y), radius) = cv2.minEnclosingCircle(c)
        #print(f"{x},{y},{radius}")
        M = cv2.moments(c)
        centre = (int(M["m10"] / M["m00"]), int(M["m01"]/M["m00"]))
        
        # only proceed if the radius meets minimum size
        if radius > 10:
            # draw the circle and centroid on the frame, then update the list of the tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),(0,255,255),2)
            cv2.circle(frame, center, 5, (0,0,255), -1)
    # update the points queue
    pts.appendleft(center)
    
    # loop over the set of tracked points
    for i in range(1, len(pts)):
        # if either of the tracked points are None, ignore
        if pts[i - 1] is None or pts[i] is None:
            continue
        
        # otherwise, compute the thickness of the line and draw the connecting lines
        thickness = int(np.sqrt(buffer/ float(i + 1)) * 2.5)
        cv.line(frame, pts[i-1],pts[i], (0,0,255), thickness)
        
    # show frame to our screen
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):
        break
    
# release the camera
vs.stop()
    
# close all windows
cv2.destroyAllWindows()
    
    