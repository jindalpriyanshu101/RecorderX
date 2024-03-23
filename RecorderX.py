from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics


print('''\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$                                                     $
$                                                     $
$                    RecorderX                        $
$                                                     $
$           Created By: Priyanshu Jindal              $
$           Github ID: jindalpriyanshu101             $
$                                                     $q                                                                                                                                                                                            
$                                                     $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n''')


width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
#time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
#file_name = f'{time_stamp}.mp4'
file_name = input("enter output name with format: ") 
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(file_name, fourcc, 8.5, (width, height))
print("Do you want any custom key to stop recording or default one?") #chose custom key

def customkey():
    check = input("Please enter y/n: ")
    global key
    if check == 'y' or check == 'Y':
        print("\nAlright, i want you to enter your preffered key :D\nNOTE: please do not use any functional key like esc,ctrl,shift etc...\n")
        key = input("Please enter your preffered key: ")
    else:
        key = 'q'
customkey()
#fps = 8.5 is stable output; 20.0 = 3x speed
#higher the fps = faster the video speed

def customkeyerror():
    check = input("Please enter y/n: ")
    global key
    if check == 'y' or check == 'Y':
        print("Alright, please do not use any functional key like esc,ctrl,shift etc...")
        key = input("Please enter your preffered key: ")
        RecorderX()
    else:
        key = 'q'
        RecorderX()


def RecorderX():
    while True:
        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow('RecorderX - Screen Recorder', img_final)

        # cv2.imshow('webcam', frame)

        output.write(img_final)
        try:
            if cv2.waitKey(10) == ord(key): # press q to stop recording
                break
        except Exception as e:
            print("Please chose a specific character, Words can\'t be used...\n\n")
            cv2.destroyAllWindows()
            customkeyerror()
            break
RecorderX()

cv2.destroyAllWindows()

