# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from jd_project.JdDao import JdMongoClient
from jd_project.items import JdItem

class GoodsSpiderSpider(scrapy.Spider):
    name = 'goods_spider'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    def parse(self, response):
        depth = response.meta['depth']
        if(depth < 2):
            soup = BeautifulSoup(response.body, 'html.parser')
            for tag in soup.find_all('a'):
                if(tag.has_key("href")):
                    href = tag['href']
                    
                if 'javascript' not in str(href):
                    if('http' not in str(href) and 'https' not in str(href)):
                        link = 'http:' + str(href)
                    else:
                        link = str(href)
                    if('item.jd.com' in str(link)):
                        yield scrapy.Request(url = link, callback= self.parse_item, dont_filter=True)
                    else:
                        depth = depth + 1
                        yield scrapy.Request(url = link, meta={"depth": depth}, callback= self.parse, dont_filter=True)
        else:
            pass

    def parse_item(self, response):
        client = JdMongoClient()
        jditem = JdItem()
        title = response.xpath('/html/body/div[6]/div/div[2]/div[1]/text()').extract()[1];
        price = response.xpath('/html/body/div[6]/div/div[2]/div[3]/div/div[1]/div[2]/span[1]/span[2]')
        url = response.url
        jditem['name'] = title
        jditem['url'] = url
        jditem['price'] = price
        yield jditem
        

        
