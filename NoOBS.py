from vidgear.gears import CamGear
import cv2
import time
from cv2 import imshow
from cv2 import imwrite

stream = CamGear(
    source="https://youtu.be/F3t-gbmI1Ew", #YT URL
    stream_mode=True,
    logging=True 
).start()

while True:
    time.sleep(20)
    img = stream.read()
    
    if img is None:
        break
    else:
        cv2.imwrite("thumbnail.png", img) 
        