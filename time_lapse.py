# usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import datetime
import picamera
import time
import sys

def cameraCapture():

    now = datetime.datetime.now()
    now_string = now.strftime("%Y%m%d_%H%M%S")

    camera = picamera.PiCamera()
    camera.resolution = (1920, 1080)
    camera.start_preview()

    time.sleep(5)
    camera.capture("/home/pi/" + now_string + "_image.jpg")
    
    camera.stop_preview()
    camera.close()

if __name__ == '__main__':

    capture_count = 0
    argvs = sys.argv
    argc = len(argvs)

    if (argc > 0):
        capture_count = int(argvs[1])
    else:
        capture_count = 8 * 60 * 6    # 8 hours

    print("caputre count : " + str(capture_count))
    
    for num in range(0, capture_count):
        print("num of capture : " + str(num + 1))
        cameraCapture()
        time.sleep(4)
        

