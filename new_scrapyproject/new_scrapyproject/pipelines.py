import psycopg2

class PostgresPipeline:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    @classmethod
    def from_crawler(cls, crawler):
        # Class method to create an instance using the settings from the crawler
        return cls(
            host=crawler.settings.get('POSTGRES_HOST'),
            port=crawler.settings.get('POSTGRES_PORT'),
            database=crawler.settings.get('POSTGRES_DATABASE'),
            user=crawler.settings.get('POSTGRES_USER'),
            password=crawler.settings.get('POSTGRES_PASSWORD')
        )

    def open_spider(self, spider):
        # Connect to the database when the spider opens
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        # Close the connection to the database when the spider closes
        self.cursor.close()
        self.conn.close()

    def process_item(self, item, spider):
        # Insert data into the 'sreality' table
        self.cursor.execute("INSERT INTO sreality (title, image_url, url) VALUES (%s, %s, %s)", (item['title'], item['image_url'], item['url']))
        self.conn.commit()
        return item
