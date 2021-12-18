import mysql.connector

DB_NAME = "DbMysql11"

db = mysql.connector.connect(
host="localhost",
port=3305,
user=DB_NAME,
password=DB_NAME,
database=DB_NAME
)

cursor = db.cursor()
cursor.execute("SHOW TABLES")
tables = []
for x in cursor:
    tables.append(x)
for table in tables:
    cursor.execute(f"DROP TABLE {table}")
db.commit()
