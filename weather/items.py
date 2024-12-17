# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    _id = scrapy.Field()
    period = scrapy.Field()
    temperature = scrapy.Field()
    condition = scrapy.Field()
