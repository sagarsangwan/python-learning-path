import mysql.connector as sql


connection = sql.connect(
    host = "localhost",
    user = "root",
    password = "1122"
)

curser = connection.cursor()
#curser.execute("CREATE DATABASE sagar21")
curser.execute("SHOW DATABASES")
for x in curser:
    print(x)