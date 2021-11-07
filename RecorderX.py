from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import time


width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
file_name = input("enter output name with format: ") 
print("Starting RecorderX, press Q on recorder screen to stop recording....")
time.sleep(3)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height)) 
#fps = 8.5 is stable output; 20.0 = 3x speed
#higher the fps = faster the video speed


while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('RecorderX - Screen Recorder', img_final)

    output.write(img_final)
    if cv2.waitKey(10) == ord('q'): # press q to stop recording
        break
print("Recording saved in folder containing RecorderX.")
cv2.destroyAllWindows()


