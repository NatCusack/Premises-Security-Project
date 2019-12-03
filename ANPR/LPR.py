from Operation import obstructionDetection, licencePlateRecognition, gateOpen, gateClose, CleanUp
from picamera import PiCamera
import time
import cv2
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

approvedPlates = ['12G3363', '141D5227']
results = [0]
gateStatus = 0

while True:
    if GPIO.input(10) == GPIO.HIGH:
        while GPIO.input(10) == GPIO.HIGH:
            time.sleep(0.1)
        results = licencePlateRecognition()
      
        for res in results:
            if res in approvedPlates:
                gateStatus = 1
                gateOpen()
                time.sleep(5)
            else:
                print("Licence Plate Not Recognised!")
                
    if gateStatus == 1:
        distance = obstructionDetection()
        while distance < 20:
            time.sleep(0.5)
            distance = obstructionDetection()
            print(distance)
            
        print("closing")
        gateClose()
        gateStatus = 0
        
        
 



