import mysql.connector as mysql

db = mysql.connect(
    host = "192.1.57.4",
    user = "root",
    passwd = "root"
    )

print(db)