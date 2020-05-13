from picamera import PiCamera
from accessCheck import checkStatus
import time
from openalpr import Alpr
import datetime
import json

def camCapture():
    print("Starting scan", "info")
    
    print("Taking picture", "info")
    cam = PiCamera()
    cam.resolution = (1024, 768)
    cam.start_preview()
    time.sleep(2) 
    pictime = datetime.datetime.now()
    picname = pictime.strftime("../pics/%Y-%m-%d_%H-%M-%S_pic.jpg")
    print(picname)
    cam.capture(picname)
    cam.stop_preview()
    cam.close()
    return picname

def licencePlateRecognition(image_path):
    
    

    print("Scanning picture", "info")
    result = ["0"]
    readResult = []
    alpr = Alpr("gb", "/etc/openalpr/openalp.conf", "/usr/share/openalpr/runtime_data")
    if not alpr.is_loaded():
            print("Failed to load OpenALPR", "error")
            result[0] = "-1"
            return result
    results = alpr.recognize_file(image_path)
    alpr.unload()
    with open('lastscan.json', 'w+') as ls:
            ls.write(json.dumps(results, indent=4))
            ls.close()
    n_results = len(results.values()[4])
    print(n_results)
    if n_results > 0:
            print("Found {} licence plate(s)".format(n_results), "info")
           #  d
           
           
           
            
            result[0] = str(n_results)
            for i in range(n_results):
                    lp = results.values()[4][i].values()[0]
                    print(lp)
                    readResult.append(str(lp))
                    conf = results.values()[4][i].values()[1]
                    print(conf, "info")
                    readResult.append(conf)
            readResult.append(checkStatus(readResult[0]))
    else:
            print("No licence plate found", "info")
            readResult.append(-1)
            
    
    print("Finished scan", "info") 
    
    

        
    
    return readResult

