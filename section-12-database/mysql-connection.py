import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123",
    #user = "user",
    #password = "123"
    database = "exampledb"
)

cursor = db.cursor()

#cursor.execute("CREATE DATABASE exampledb")

cursor.execute("CREATE TABLE categories (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
#cursor.execute("SHOW DATABASES")

for i in cursor:
    print(i)


print(db)