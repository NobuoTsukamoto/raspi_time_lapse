# usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import datetime
import picamera

def cameraCapture():

    now = datetime.datetime.now()
    now_string = now.strftime("%Y%m%d_%H%M%S")

    camera = picamera.PiCamera()
    camera.resolution = (2592, 1944)
    camera.start_preview()

    time.sleep(5)
    camera.capture("/home/pi/" + now_string + "_image.jpg")

if __name__ == '__main__':
    cameraCapture()

