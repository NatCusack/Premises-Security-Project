import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

def gateOpen():
    
    
    
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup( 13, GPIO.OUT)
    
        
    leftGate = GPIO.PWM(12, 50)
    rightGate = GPIO.PWM(13, 50)
    leftGate.start(0)
    rightGate.start(0)

    print("Opening gates")
    
    
    leftGate.ChangeDutyCycle(8)
    rightGate.ChangeDutyCycle(8)
    time.sleep(0.5)
    leftGate.ChangeDutyCycle(0)
    rightGate.ChangeDutyCycle(0)
    
    GPIO.cleanup(12)
    GPIO.cleanup(13)

def gateClose():
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup( 13, GPIO.OUT)
    
    
    leftGate = GPIO.PWM(12, 50)
    rightGate = GPIO.PWM(13, 50)
    leftGate.start(0)
    rightGate.start(0)
    
    print("Closing gates")

    leftGate.ChangeDutyCycle(3)
    rightGate.ChangeDutyCycle(13)
    time.sleep(0.5)
    leftGate.ChangeDutyCycle(0)
    rightGate.ChangeDutyCycle(0)
    
    GPIO.cleanup(12)
    GPIO.cleanup(13)
    
gateClose()

