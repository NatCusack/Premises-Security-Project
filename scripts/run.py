import time
from  licenceScan import licencePlateRecognition, camCapture
from alprDatabase import addLatestScan
from motionDetection import motionDetection, obstructionDetection
from Email import sendmail
from gateOperation import gateOpen, gateClose

while(1):
    if(motionDetection() == True):
        print("Motion Detected")
        image = camCapture()
        results = licencePlateRecognition(image)
        
        if results[0] != -1:
            addLatestScan(results, image)
            if results[2]  == "Approved":
                gateOpen()
                time.sleep(2)
                obstructionDetection()
                gateClose()
            
            elif results[2] == "Blocked":
                sendmail(results[0])
                


            
                
                
            
                
        
    


