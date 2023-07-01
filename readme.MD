# Sreality.cz Scraper

This project consists of a Scrapy spider for sreality.cz and a Flask application to display the scraped data. The spider scrapes the first 500 apartment sale ads (title, image url), saves them to a PostgreSQL database, and the Flask application displays these ads.

## Files

- `requirements.txt`: This file lists all Python dependencies.

- `docker-compose.yml`: Configuration file to manage the services of the Docker application.

- `init.sql`: SQL script to create the necessary database and table in PostgreSQL.

- `entrypoint.sh`: Shell script that waits for the database to become available, then runs the SQL script and the Flask application.

### Web

- `server.py`: Flask application that connects to the database and displays the scraped ads.

- `Dockerfile`: Instructions for building the Docker image for the Flask application.

- `templates/index.html`: HTML template for the Flask application.

### New Scrapy Project

- `settings.py`: Settings for the Scrapy spider, such as the database connection parameters.

- `items.py`: Defines the fields for the scraped items.

- `middlewares.py`: Custom middleware for the Scrapy spider.

- `pipelines.py`: Pipeline for storing scraped items in the PostgreSQL database.

- `spiders/sreality.py`: The Scrapy spider that scrapes sreality.cz.

- `Dockerfile`: Instructions for building the Docker image for the Scrapy spider.

## Running the application

To run the application, clone the repository and run `docker-compose up`.

The scraped ads can be viewed at http://127.0.0.1:8080.
