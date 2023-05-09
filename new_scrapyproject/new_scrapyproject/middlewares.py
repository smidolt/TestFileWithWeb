import logging
from scrapy import signals
from itemadapter import is_item, ItemAdapter

class ScrapyprojectSpiderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_output(self, response, result, spider):
        for i in result:
            if is_item(i):
                # добавление поля url к каждому элементу
                i['url'] = response.url
            yield i

    def spider_opened(self, spider):
        logging.info(f"Spider opened: {spider.name}")

class ScrapyprojectDownloaderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_response(self, request, response, spider):
        if response.status != 200:
            # Log an error if the response status is not 200
            logging.error(f"Failed to download {request.url}: {response.status}")
        return response

    def spider_opened(self, spider):
        # This method is called when a spider is opened
        logging.info(f"Spider opened: {spider.name}")
