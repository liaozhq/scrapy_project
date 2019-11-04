# -*- coding: utf-8 -*-
import scrapy
from jd_project.items import JdItem

class ItemSpiderSpider(scrapy.Spider):
    name = 'item_spider'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']
    def start_requests(self):
        req = []
        cnt = 1
        for i in range(0, 100):
            if i > 0:
               page = cnt + i*2
               req.append(scrapy.Request('https://search.jd.com/Search?keyword=梨子&enc=utf-8&page='+str(page)))
        return req

    def parse(self, response):
        lis = response.xpath('//*[@id="J_goodsList"]/ul/li')
        for li in lis:
            name = li.xpath('div/div[1]/a/@title').extract_first()
            href = li.xpath('div/div[1]/a/@href').extract_first()
            price = li.xpath('div/div[2]/strong/i/text()').extract_first()
            item = JdItem()
            item['name'] = name
            item['url'] = href
            item['price'] = price 
            yield scrapy.Request(url = "http:"+str(href), meta={"item":item}, callback= self.parse_item, dont_filter=True)
            #yield item

    def parse_item(self, response):
        item = response.meta["item"]
        yield item


