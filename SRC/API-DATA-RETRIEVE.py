import requests
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

def get_winning_titles():
    url = "https://imdb8.p.rapidapi.com/title/get-best-picture-winners"

    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': ""
        }

    response = requests.request("GET", url, headers=headers).json()

    title_ids = []
    for item in response:
        id = item.split('/')[2]
        title_ids.append(id)

    return title_ids

def create_table_best_picture_winners():
    title_ids = get_winning_titles()
    cursor.execute("CREATE TABLE best_picture_winners (id VARCHAR(255) PRIMARY KEY)")
    for id in title_ids:
        sql = "INSERT INTO best_picture_winners VALUES (%s)"
        cursor.execute(sql,(id,))
        db.commit()


try:
    create_table_best_picture_winners()
except: 
    print("an error occurred")
    db.rollback()

cursor.close()
db.close()
