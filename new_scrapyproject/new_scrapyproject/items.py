import scrapy

class SrealityItem(scrapy.Item):
    # Define the fields for your item here:
    title = scrapy.Field()       # Title of the item
    image_url = scrapy.Field()   # URL of the item's image
    price = scrapy.Field()       # Price of the item
    url = scrapy.Field()         # URL of the item's ad (additional field for storing the ad address)
