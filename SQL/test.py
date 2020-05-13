import pymysql

connection = pymysql.connect(host = "192.168.43.194",
                     user = "anpr",
                     password = "root",
                     db = "psp")

cursor = connection.cursor()

cursor.execute("SELECT VERSION()")

connection.close()