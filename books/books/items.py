import scrapy

class BooksItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
