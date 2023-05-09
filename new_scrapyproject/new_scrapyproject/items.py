import scrapy

class SrealityItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    image_url = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()  # добавление поля url для хранения адреса объявления
