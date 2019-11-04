# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field() #mongodb自动生成id必要
    name = scrapy.Field() #商品名称
    price = scrapy.Field() #商品价格
    images = scrapy.Field() #商品图片
    url = scrapy.Field()
    

    
