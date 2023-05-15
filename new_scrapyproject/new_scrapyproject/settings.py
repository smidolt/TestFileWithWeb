import os
from dotenv import load_dotenv
load_dotenv()

# The name of the project
BOT_NAME = "new_scrapyproject"

# The modules where spiders are located
SPIDER_MODULES = ['new_scrapyproject.spiders']
NEWSPIDER_MODULE = "new_scrapyproject.spiders"

# Whether to obey robots.txt rules
ROBOTSTXT_OBEY = True

# The encoding of the feed export
FEED_EXPORT_ENCODING = "utf-8"

# PostgreSQL database connection parameters
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "172.29.0.2")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE", "sreality")
POSTGRES_USER = os.getenv("POSTGRES_USER", "example")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "example")

# Activation of pipeline for saving data to the database
ITEM_PIPELINES = {
   'new_scrapyproject.pipelines.PostgresPipeline': 300,
}

# Setting the User-Agent header for all requests
USER_AGENT = 'new_scrapyproject (+http://www.yourdomain.com)'

# Limit on the number of simultaneous requests
CONCURRENT_REQUESTS = 16
