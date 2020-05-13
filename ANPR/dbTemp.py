from picamera import PiCamera
import RPi.GPIO as GPIO
import time
from openalpr import Alpr
import datetime
import json
import pymysql

 
print("initialising")



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

def AddToDatabase(licencePlate):
    connection = pymysql.connect(host = "192.168.43.194",
                     user = "anpr",
                     password = "root",
                     db = "psp")

    cursor = connection.cursor()
    sql = "Insert Into 'plates'('licenceplate', 'accessdate', 'accessGranted') VALUES ('"+ licencePlate +"','09051995',0)"
    cursor.execute(sql)
    connection.commit()
    
    connection.close()
    
    


