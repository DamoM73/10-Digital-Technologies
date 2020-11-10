# get HSV values
from __future__ import division
import cv2
import numpy as np
import time
from imutils.video import VideoStream

def nothing(*arg):
    pass

# Initial HSV GUI slider values to load on program start.
icol = (89, 0, 0, 125, 255, 255)   
cv2.namedWindow('colorTest')
# Create lower range colour sliders
cv2.createTrackbar('lowHue', 'colorTest', icol[0], 255, nothing)
cv2.createTrackbar('lowSat', 'colorTest', icol[1], 255, nothing)
cv2.createTrackbar('lowVal', 'colorTest', icol[2], 255, nothing)
# Create higher range colour sliders.
cv2.createTrackbar('highHue', 'colorTest', icol[3], 255, nothing)
cv2.createTrackbar('highSat', 'colorTest', icol[4], 255, nothing)
cv2.createTrackbar('highVal', 'colorTest', icol[5], 255, nothing)

# connect to camera
frame_size = (320,240)
capture = VideoStream(src=0, usePiCamera=True, resolution=frame_size, framerate=32).start()
time.sleep(0.5)

while True:
    # Get HSV values from the GUI sliders.
    lowHue = cv2.getTrackbarPos('lowHue', 'colorTest')
    lowSat = cv2.getTrackbarPos('lowSat', 'colorTest')
    lowVal = cv2.getTrackbarPos('lowVal', 'colorTest')
    highHue = cv2.getTrackbarPos('highHue', 'colorTest')
    highSat = cv2.getTrackbarPos('highSat', 'colorTest')
    highVal = cv2.getTrackbarPos('highVal', 'colorTest')

    # grab an image of current frame from the camera
    frame = capture.read()
    frame = cv2.flip(frame, -1)
    
    # Show the original image.
    cv2.imshow('frame', frame)
        
    # Blur methods available, comment or uncomment to try different blur methods.
    #frameBGR = cv2.GaussianBlur(frame, (7, 7), 0)
    #frameBGR = cv2.medianBlur(frame, 7)
    frameBGR = cv2.bilateralFilter(frame, 15 ,75, 75)
    """kernal = np.ones((15, 15), np.float32)/255
    frameBGR = cv2.filter2D(frame, -1, kernal)"""
    
    # Show blurred image.
    cv2.imshow('blurred', frameBGR)
    
    # HSV (Hue, Saturation, Value).
    # Convert the frame to HSV colour model.
    frameHSV = cv2.cvtColor(frameBGR, cv2.COLOR_BGR2HSV)
    
    # HSV values to define a colour range we want to create a mask from.
    colorLow = np.array([lowHue,lowSat,lowVal])
    colorHigh = np.array([highHue,highSat,highVal])
    mask = cv2.inRange(frameHSV, colorLow, colorHigh)
    # Show the first mask
    cv2.imshow('mask-plain', mask)

    # Cleanup the mask with Morphological Transformation functions
    kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

    # Show morphological transformation mask
    cv2.imshow('mask', mask)
    
    # Put mask over top of the original image.
    result = cv2.bitwise_and(frame, frame, mask = mask)

    # Show final output image
    cv2.imshow('colorTest', result)
    
    # listen for exit key (q) to eixt main loop
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# close program
cv2.destroyAllWindows()
capture.stop()