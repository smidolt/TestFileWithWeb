from flask import Flask, render_template
import psycopg2
import time
import os

app = Flask(__name__)
conn = None

def wait_for_db_connection():
    global conn
    while True:
        try:
            conn = psycopg2.connect(dbname="sreality", user="example", password="example", host="db")
            break
        except psycopg2.OperationalError as e:
            print("Waiting for database connection...")
            time.sleep(5)
wait_for_db_connection()

@app.route('/')
def index():
    with conn.cursor() as cursor:
        cursor.execute("SELECT title, image_url FROM sreality")
        items = cursor.fetchall()
    print(items)
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
