import mysql.connector
import pandas as pd

DB_NAME = "DbMysql11"

db = mysql.connector.connect(
    host="localhost",
    port=3305,
    user=DB_NAME,
    password=DB_NAME,
    database=DB_NAME
    )

cursor = db.cursor()

def create_table(create_sql, table_name, cols):
    s = ("%s,"*cols)[:-1]
    df = pd.read_csv(f"./data/{table_name}.csv", index_col=False, delimiter = ',')
    cursor.execute(create_sql)
    for i, row in df.iterrows():
        sql = f"INSERT INTO {table_name} VALUES ({s})"
        cursor.execute(sql, tuple(row))
        db.commit()

def create_table_movie():
    create_table(sql, "movie", 5)

def create_table_rating():
    sql = "CREATE TABLE rating(id VARCHAR(255) PRIMARY KEY,mean_vote INT,total_votes INT)"
    create_table(sql, "rating", 3)

def create_table_person():
    sql = "CREATE TABLE person(id VARCHAR(255) PRIMARY KEY,name VARCHAR(255),date_of_death DATE,birthplace VARCHAR(255))"
    create_table(sql, "person", 4)

def create_table_principal():
    sql = "CREATE TABLE principal(id VARCHAR(255) PRIMARY KEY,name VARCHAR(255),category VARCHAR(255))"
    create_table(sql, "principal", 3)
