from vidgear.gears import CamGear
import cv2
import time
from cv2 import imshow
from cv2 import imwrite



while True:
    
    time.sleep(20)
    stream = CamGear(
    source="https://youtu.be/4KjavYG_AEI", #YT URL
    stream_mode=True,
    logging=True 
                ).start()
    
    time.sleep(1)
    img = stream.read()
    
    if img is None:
        print("Error")
        break
    else:
        cv2.imwrite("thumbnail.png", img) 
        print("imwrite")
        
    
    
    stream.stop() 
             
# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()           