import pymysql

connection = pymysql.connect(host = "192.168.1.11",
                     user = "anpr",
                     password = "root",
                     db = "psp")

cursor = connection.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()
print("Database version : %s " % data)

#connection.close()

try:
#    with connection.cursor() as cursor:
#        sql = "Insert Into 'plates'('licenceplate', 'accessdate', 'accessGranted') VALUES ('192T4213','09051995',0)"
#        cursor.execute(sql)
#        connection.commit()
        
        with connection.cursor() as cursor:
            sql = "SELECT `accessdate`, `licenceplate` FROM `plates`"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
finally:
    connection.close()