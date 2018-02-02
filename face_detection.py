# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 15:23:15 2018

@author: Manuel
"""

import dlib # dlib for accurate face detection
import cv2 # opencv
import imutils # helper functions from pyimagesearch.com
import serial
import time

## Grab video from your webcam
stream = cv2.VideoCapture(0)
 
## Face detector
detector = dlib.get_frontal_face_detector()

## Set up serial communication
commport = input("Enter port: ")
#ser = serial.Serial(commport , 115200)

## Fancy box drawing function
def draw_border(img, pt1, pt2, color, thickness, r, d):
    x1, y1 = pt1
    x2, y2 = pt2
 
    # Top left drawing
    cv2.line(img, (x1 + r, y1), (x1 + r + d, y1), color, thickness)
    cv2.line(img, (x1, y1 + r), (x1, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x1 + r, y1 + r), (r, r), 180, 0, 90, color, thickness)
 
    # Top right drawing
    cv2.line(img, (x2 - r, y1), (x2 - r - d, y1), color, thickness)
    cv2.line(img, (x2, y1 + r), (x2, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x2 - r, y1 + r), (r, r), 270, 0, 90, color, thickness)
 
    # Bottom left drawing
    cv2.line(img, (x1 + r, y2), (x1 + r + d, y2), color, thickness)
    cv2.line(img, (x1, y2 - r), (x1, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x1 + r, y2 - r), (r, r), 90, 0, 90, color, thickness)
 
    # Bottom right drawing
    cv2.line(img, (x2 - r, y2), (x2 - r - d, y2), color, thickness)
    cv2.line(img, (x2, y2 - r), (x2, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x2 - r, y2 - r), (r, r), 0, 0, 90, color, thickness)

## Face Detection Loop
x1, x2, y1, y2 = 0, 1, 0, 1
width = 1280
height = 720

while True:
    # read frames from live web cam stream
    (grabbed, frame) = stream.read()
 
    # resize the frames to be smaller and switch to gray scale
    frame = imutils.resize(frame, width= width, height = height)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    # Make copies of the frame for transparency processing
    overlay = frame.copy()
    output = frame.copy()
 
    # set transparency value
    alpha  = 0.5
 
    # detect faces in the gray scale frame
    face_rects = detector(gray, 0)
 
    if len(face_rects) > 0:
   
        # loop over the face detections 
        #for i, d in enumerate(face_rects):
        #   x1, y1, x2, y2, w, h = d.left(), d.top(), d.right(), d.bottom(), d.width(), d.height()
    
        d = face_rects[0]
        x1, y1, x2, y2, w, h = d.left(), d.top(), d.right(), d.bottom(), d.width(), d.height()

        # draw a fancy border around the faces
        draw_border(overlay, (x1, y1), (x2, y2), (100, 255, 0), 2, 10, 10)
        cv2.circle(overlay, (int(width/2), int(height/2)), 5, (100, 255, 0), 2)
   
        # make semi-transparent bounding box
        cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)

        # Face location
        face_center = [abs(x1+x2/2), abs(y1+y2/2)]
        x_offset_center = face_center[0] - width/2
        y_offset_center = face_center[1] - height/2

    else:
        x_offset_center = 0
        y_offset_center = 0

    # show the frame
    cv2.imshow("Face Detection", output)
    key = cv2.waitKey(1) & 0xFF
 
    # press q to break out of the loop
    if key == ord("q"):
        break
    
    

    print(x_offset_center)
   # ser.write(x_offset_center)
   # ser.write(y_offset_center)

# cleanup
cv2.destroyAllWindows()
stream.stop()
