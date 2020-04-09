import mysql.connector as mysql

db = mysql.connect(
    host = "192.168.43.194",
    user = "anpr",
    passwd = "root"
    )

print(db)

cursor = db.cursor()

cursor.execute("SHOW DATABASES")


databases = cursor.fetchall()


print(databases)


for database in databases:
    print(database)