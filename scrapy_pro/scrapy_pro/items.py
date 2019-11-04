# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class XiciItem(scrapy.Item):
    _id = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()
    address = scrapy.Field()
    flage = scrapy.Field()
    type = scrapy.Field()
    speed = scrapy.Field()
    check_time = scrapy.Field()
