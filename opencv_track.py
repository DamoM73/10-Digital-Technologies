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
ap.add_argument('-v', '--video', help='path to the (optional) video file')
ap.add_argument('-b', '--buffer', type=int, default=64, help='max buffer size')
args = vars(ap.parse_args())