# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from jd_project.spiders.item_spider import ItemSpiderSpider
from jd_project.spiders.goods_spider import GoodsSpiderSpider
from jd_project.JdDao import JdMongoClient

class JdProjectPipeline(object):
    def process_item(self, item, spider):
        client = JdMongoClient()
        if (isinstance(spider, GoodsSpiderSpider) or isinstance(spider, ItemSpiderSpider)):
            client.insertJD(item)
        return item
