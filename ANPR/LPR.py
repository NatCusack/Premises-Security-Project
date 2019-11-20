from Operation import obstructionDetection, licencePlateRecognition, gateOpen, gateClose, CleanUp
from picamera import PiCamera
import time
import cv2
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(10) == GPIO.HIGH:
        while GPIO.input(10) == GPIO.HIGH:
            time.sleep(0.1)
        print("Button Was Pressed")


licencePlateRecognition()
gateClose()
print(obstructionDetection())
CleanUp()


