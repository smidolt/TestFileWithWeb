from flask import Flask, render_template
import psycopg2
import time
import os

app = Flask(__name__)  # Create a new Flask web server instance
conn = None  # Initialize the connection to the database as None

def wait_for_db_connection():
    global conn  # Use the global conn variable
    while True:
        try:
            # Try to establish a connection to the database
            conn = psycopg2.connect(dbname="sreality", user="example", password="example", host="db")
            break  # If the connection is successful, break the loop
        except psycopg2.OperationalError as e:
            # If the connection fails, print a message and wait 5 seconds before trying again
            print("Waiting for database connection...")
            time.sleep(5)
wait_for_db_connection()  # Call the function to wait for a connection to the database

@app.route('/')  # Define the route for the index page
def index():
    with conn.cursor() as cursor:  # Get a cursor from the database connection
        # Execute a query to select the title and image_url from the sreality table
        cursor.execute("SELECT title, image_url FROM sreality")
        items = cursor.fetchall()  # Fetch all rows returned by the query
    print(items)  # Print the fetched items
    # Render the index.html template and pass the items to it
    return render_template('index.html', items=items)

if __name__ == '__main__':
    # If this script is run directly, start the Flask web server
    app.run(host='0.0.0.0', port=8080)
