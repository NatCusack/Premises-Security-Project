import json

def checkStatus(plate):
    
    with open("../approved.json", "rb") as json_file:
        data = json.load(json_file)
        for approvedPlates in data:
            if plate in approvedPlates["plate"]:
                print(plate)
                print(approvedPlates["plate"])
                print("True")
                return "Approved"
            
    with open ("../blocked.json", "rb") as json_file:
        data = json.load(json_file)
        for blockedPlates in data:
            if plate in blockedPlates["plate"]:
                print("Plate " + plate +" Blocked!")
                return "Blocked"
    
    return "Unknown"
                