import logging
from scrapy import signals
from itemadapter import is_item, ItemAdapter

class ScrapyprojectSpiderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        # Class method to get a new instance from the crawler
        s = cls()
        # Connect the spider_opened signal to a method
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_output(self, response, result, spider):
        # Process the output from the spider
        for i in result:
            if is_item(i):
                # Add url field to each item
                i['url'] = response.url
            yield i

    def spider_opened(self, spider):
        # Method called when the spider is opened
        logging.info(f"Spider opened: {spider.name}")

class ScrapyprojectDownloaderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        # Class method to get a new instance from the crawler
        s = cls()
        # Connect the spider_opened signal to a method
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_response(self, request, response, spider):
        # Process the response from a spider
        if response.status != 200:
            # Log an error if the response status is not 200
            logging.error(f"Failed to download {request.url}: {response.status}")
        return response

    def spider_opened(self, spider):
        # Method called when the spider is opened
        logging.info(f"Spider opened: {spider.name}")
