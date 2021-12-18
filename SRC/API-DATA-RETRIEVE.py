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
        'x-rapidapi-key': "150f682d97msh51191443c0a7f97p15f58fjsn85b98d4e5490"
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

    # cursor.execute("SELECT * FROM best_picture_winners")
    # for x in cursor:
    #     print(x)
