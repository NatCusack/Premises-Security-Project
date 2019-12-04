from picamera import PiCamera
from time import sleep
from openalpr import Alpr
import datetime
import json
import log

def scan():
	log.write("Starting scan", "info")
	
	log.write("Taking picture", "info")
	cam = PiCamera()
	cam.start_preview()
	sleep(2)
	pictime = datetime.datetime.now()
	picname = pictime.strftime("pics/%Y-%m-%d_%H-%M-%S_pic.jpg")
	cam.capture(picname)
	cam.stop_preview()
	cam.close()
	
	log.write("Scanning picture", "info")
	result = ["0"]
	alpr = Alpr("eu", "/etc/openalpr/openalp.conf", "/usr/share/openalpr/runtime_data")
	if not alpr.is_loaded():
		log.write("Failed to load OpenALPR", "error")
		result[0] = "-1"
		return result
	results = alpr.recognize_file(picname)
	alpr.unload()
	with open('lastscan.json', 'w+') as ls:
		ls.write(json.dumps(results, indent=4))
		ls.close()
	n_results = len(results.values()[4])
	if n_results > 0:
		log.write("Found {} licence plate(s)".format(n_results), "info")
		result[0] = str(n_results)
		for i in range(n_results):
			lp = results.values()[4][i].values()[0]
			log.write(lp, "info")
			result.append(lp)
	else:
		log.write("No licence plate found", "info")
	
	log.write("Finished scan", "info")
	return result
