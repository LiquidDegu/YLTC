from email.mime import image
from unittest import result
import cv2
from cv2 import VideoCapture
from cv2 import imshow
from cv2 import imwrite

cam = VideoCapture(1, cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


r, img = cam.read()




if r:

    imshow("Test", img)
    imwrite("Test.png", img)
else:
    print("No image")