# -*- coding: utf-8 -*-
import scrapy
from scrapy_pro.items import XiciItem


class XicispiderSpider(scrapy.Spider):
    name = 'xicispider'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://xicidaili.com/']

    def start_requests(self):

        req = []

        for num in range(1, 3794):
            request = scrapy.Request('http://www.xicidaili.com/nn/'+str(num))
            req.append(request)   

        return req

    def parse(self, response):
        
        ip_list = response.xpath('//*[@id="ip_list"]')

        items = []

        trs = ip_list.xpath('tr')

        for tr in trs:
            xiciItem = XiciItem()
            xiciItem['ip'] = tr.xpath('td[2]/text()').extract_first()
            
            xiciItem['port'] = tr.xpath('td[3]/text()').extract_first()
            
            xiciItem['address'] = tr.xpath('string(td[4])')[0].extract().strip()

            xiciItem['flage'] = tr.xpath('string(td[5])')[0].extract()
            
            xiciItem['type'] = tr.xpath('string(td[6])')[0].extract()
            
            # xiciItem['speed'] = tr.xpath(
            #     'td[7]/div[@class="bar"]/@title').re('\d{0,2}\.\d{0,}')[0]
                
            # xiciItem['check_time'] = tr.xpath('td[10]/text()')[0].extract()
            items.append(xiciItem)
        
        return items