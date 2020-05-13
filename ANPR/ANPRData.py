from picamera import PiCamera
import time
from openalpr import Alpr
import datetime
import json
import cv2 as cv

def licencePlateRecognition():
    img = cv.imread('car.jpg', cv.IMREAD_UNCHANGED)   
    print("Scanning picture", "info")
    result = ["0"]
    alpr = Alpr("gb", "/etc/openalpr/openalp.conf", "/usr/share/openalpr/runtime_data")
    if not alpr.is_loaded():
            print("Failed to load OpenALPR", "error")
            result[0] = "-1"
            return result
    results = alpr.recognize_file("car.jpeg")
    alpr.unload()
    with open('lastscan.json', 'w+') as ls:
            ls.write(json.dumps(results, indent=4))
            ls.close()
    n_results = len(results.values()[4])
    if n_results > 0:
            print("Found {} licence plate(s)".format(n_results), "info")
            readResult = []
            result[0] = str(n_results)
            for i in range(n_results):
                    lp = results.values()[4][i].values()[0]
                    print(lp)
                    readResult.append(str(lp))
                    conf = results.values()[4][i].values()[1]
                    print(conf, "info")
                    readResult.append(conf)
    else:
            print("No licence plate found", "info")
    
    print("Finished scan", "info")
    print(readResult)
    return readResult
res = licencePlateRecognition()
print("Plate: " + res[0])
print("Confidence: %.2f" % res[1])
