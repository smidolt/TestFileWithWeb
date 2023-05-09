import os
from dotenv import load_dotenv
load_dotenv()

# The name of the project
BOT_NAME = "new_scrapyproject"

# The modules where to look for spiders
SPIDER_MODULES = ['new_scrapyproject.spiders']
NEWSPIDER_MODULE = "new_scrapyproject.spiders"

# Whether to obey robots.txt rules
ROBOTSTXT_OBEY = False

# # The implementation of request fingerprinting
# REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"

# The encoding of the feed export
FEED_EXPORT_ENCODING = "utf-8"

# Параметры подключения к базе данных PostgreSQL
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "172.29.0.2")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE", "sreality")
POSTGRES_USER = os.getenv("POSTGRES_USER", "example")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "example")

# Активация pipeline для сохранения данных в базу данных
ITEM_PIPELINES = {
   'new_scrapyproject.pipelines.PostgresPipeline': 300,
}

# Установка заголовка User-Agent для всех запросов
USER_AGENT = 'new_scrapyproject (+http://www.yourdomain.com)'

# Ограничение количества одновременных запросов
CONCURRENT_REQUESTS = 16
