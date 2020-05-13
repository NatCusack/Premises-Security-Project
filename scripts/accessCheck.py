import json

def checkStatus(plate):
    
    with open("../approvedPlates.json", "rb") as json_file:
        data = json.load(json_file)
        for approvedPlates in data["approved"]:
            #for i in approvedPlates["plate"]:
            if plate in approvedPlates["plate"]:
                print(plate)
                print(approvedPlates["plate"])
                print("True")
                return "Approved"
            
        for blockedPlates in data["blocked"]:
            if plate in blockedPlates["plate"]:
                print("Plate " + plate +" Blocked!")
                return "Blocked"
            else:
                return "Unknown"
                
            
        
# checkStatus("4D6939")
# checkStatus("131CE2222")