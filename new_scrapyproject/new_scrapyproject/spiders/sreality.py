import scrapy
from ..items import SrealityItem

class SrealitySpider(scrapy.Spider):
    name = "sreality"    # Name of the spider
    start_urls = ['https://www.sreality.cz/en/search/for-sale/apartments/all-countries']    # Initial URL to crawl
    counter = 0    # Counter to keep track of the number of ads processed

    def parse(self, response):
        # Parsing method to extract data from the response
        for ad in response.css('div.property-list__item'):
            # Stop parsing if the counter reaches 500
            if self.counter >= 500:
                break

            # Create a new SrealityItem and populate its fields
            item = SrealityItem()
            item['title'] = ad.css('.name::text').get().strip() or ''
            item['image_url'] = ad.css('.property-image::attr(src)').get() or ''
            item['price'] = ad.css('.norm-price::text').get().replace('\xa0', ' ') or ''
            # Increase the counter by 1
            self.counter += 1
            # Yield the item to the Scrapy engine
            yield item

        # If the counter is less than 500, follow the next page link
        if self.counter < 500:
            next_page = response.css('.next::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
