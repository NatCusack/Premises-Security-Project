import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
TRIG1 = 16
ECHO1 = 18

TRIG2 = 26
ECHO2= 24

GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(TRIG2,GPIO.OUT)

GPIO.output(TRIG1, 0)
GPIO.output(TRIG2, 0)


GPIO.setup(ECHO1, GPIO.IN)
GPIO.setup(ECHO2, GPIO.IN)
time.sleep(0.1)

def obstructionDetection():
    GPIO.setup(ECHO2, GPIO.IN)
    time.sleep(0.1)

    print("Starting Measurement..")
    
    distance = 0
    
    while distance < 10:

        GPIO.output(TRIG2,1)
        time.sleep(0.0001)
        GPIO.output(TRIG2,0)

        while GPIO.input(ECHO2) ==0:
                pass
        start = time.time()

        while GPIO.input(ECHO2) ==1:
                pass
        stop = time.time()

        distance = (stop - start) * 17000
    
    print("Obstruction Cleared!")
        
    

def motionDetection():
    GPIO.setmode(GPIO.BOARD)
     
    GPIO.setup(ECHO1, GPIO.IN)
    time.sleep(0.1)

    
    while(1):
        GPIO.output(TRIG1,1)
        time.sleep(0.0001)
        GPIO.output(TRIG1,0)

        while GPIO.input(ECHO1) ==0:
                pass
        start = time.time()

        while GPIO.input(ECHO1) ==1:
                pass
        stop = time.time()

        distance1 = (stop - start) * 17000
        
        GPIO.output(TRIG1,1)
        time.sleep(0.0001)
        GPIO.output(TRIG1,0)

        while GPIO.input(ECHO1) ==0:
                pass
        start = time.time()

        while GPIO.input(ECHO1) ==1:
                pass
        stop = time.time()

        distance2 = (stop - start) * 17000
        
        if((distance1 - distance2) > 10):
            print("Car Approaching")
            return True