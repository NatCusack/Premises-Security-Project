import pymysql
import mysql.connector
import datetime

def photoToBinary(photo_path):
    with open(photo_path, "rb") as image:
        binaryData = image.read()
    return binaryData






def addLatestScan(results,path_to_image):
    
    connection = mysql.connector.connect(host = "192.168.1.2",
                     user = "anpr",
                     password = "root",
                     db = "psp")
    
    
    
    try:
        cursor = connection.cursor()
        sql = """Insert Into plates(licenceplate,confidence,accesstime,accessGranted,image) VALUES (%s,%s,%s,%s,%s)"""
        
        binarydata =photoToBinary(path_to_image)
        plate = results[0]
        conf = results[1]
        access = results[2]
        date = datetime.datetime.now()
        insert_tuple = (plate, conf, date, access, binarydata  )
        
        cursor.execute(sql, insert_tuple)
        connection.commit()
            
    finally:
        connection.close()

