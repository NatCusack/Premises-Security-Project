from picamera import PiCamera
import RPi.GPIO as GPIO
import time
from openalpr import Alpr
import datetime
import json

 
print("initialising")

GPIO.setmode(GPIO.BOARD)
TRIG = 16
ECHO = 18

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup( 13, GPIO.OUT)

GPIO.output(TRIG, 0)



leftGate = GPIO.PWM(12, 50)
rightGate = GPIO.PWM(13, 50)


GPIO.setup(ECHO, GPIO.IN)
time.sleep(0.1)

leftGate.start(0)
rightGate.start(0)

def gateOpen():
    
    print("Opening gates")
    
    
    leftGate.ChangeDutyCycle(2)
    rightGate.ChangeDutyCycle(10)
    time.sleep(0.5)
    leftGate.ChangeDutyCycle(0)
    rightGate.ChangeDutyCycle(0)
    
    
        
def gateClose():
    print("Closing gates")

    leftGate.ChangeDutyCycle(10)
    rightGate.ChangeDutyCycle(2)
    time.sleep(0.5)
    leftGate.ChangeDutyCycle(0)
    rightGate.ChangeDutyCycle(0)

def obstructionDetection():
    GPIO.setup(ECHO, GPIO.IN)
    time.sleep(0.1)

    print("Starting Measurement..")
    

    GPIO.output(TRIG,1)
    time.sleep(0.0001)
    GPIO.output(TRIG,0)

    while GPIO.input(ECHO) ==0:
            pass
    start = time.time()

    while GPIO.input(ECHO) ==1:
            pass
    stop = time.time()

    distance = (stop - start) * 17000
    
    return distance



def licencePlateRecognition():
    print("Starting scan", "info")
    
    print("Taking picture", "info")
    cam = PiCamera()
    cam.resolution = (1024, 768)
    cam.start_preview()
    time.sleep(2)
    pictime = datetime.datetime.now()
    picname = pictime.strftime("pics/%Y-%m-%d_%H-%M-%S_pic.jpg")
    print(picname)
    cam.capture(picname)
    cam.stop_preview()
    cam.close()
    
    print("Scanning picture", "info")
    result = ["0"]
    alpr = Alpr("gb", "/etc/openalpr/openalp.conf", "/usr/share/openalpr/runtime_data")
    if not alpr.is_loaded():
            print("Failed to load OpenALPR", "error")
            result[0] = "-1"
            return result
    results = alpr.recognize_file(picname)
    alpr.unload()
    with open('lastscan.json', 'w+') as ls:
            ls.write(json.dumps(results, indent=4))
            ls.close()
    n_results = len(results.values()[4])
    if n_results > 0:
            print("Found {} licence plate(s)".format(n_results), "info")
            result[0] = str(n_results)
            for i in range(n_results):
                    lp = results.values()[4][i].values()[0]
                    print(lp, "info")
                    result.append(lp)
    else:
            print("No licence plate found", "info")
    
    print("Finished scan", "info")
    return result

def CleanUp():
    GPIO.cleanup()

