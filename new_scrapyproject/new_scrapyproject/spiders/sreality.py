import scrapy
from ..items import SrealityItem

class SrealitySpider(scrapy.Spider):
    name = "sreality"
    start_urls = ['https://www.sreality.cz/en/search/for-sale/apartments/all-countries']
    counter = 0

    def parse(self, response):
        for ad in response.css('div.property-list__item'):
            if self.counter >= 500:
                break

            item = SrealityItem()
            item['title'] = ad.css('.name::text').get().strip() or ''
            item['image_url'] = ad.css('.property-image::attr(src)').get() or ''
            item['price'] = ad.css('.norm-price::text').get().replace('\xa0', ' ') or ''
            self.counter += 1
            yield item

        if self.counter < 500:
            next_page = response.css('.next::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
