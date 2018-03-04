# -*- coding: utf-8 -*-
import scrapy
from ..items import  BileiSpiderItem


class IcodropSpider(scrapy.Spider):
    name = 'icodrops'
    allowed_domains = ['icodrop.com']
    start_urls = ['https://icodrops.com/syncfab/']

    def parse(self, response):
        item = BileiSpiderItem()
        ico_icon = response.xpath("//div[@class='ico-icon']/img/@src").extract()
        ico_name = response.xpath("//div[@class='ico-main-info']/h3/text()").extract()[0]
        ico_category = response.xpath("//span[@class='ico-category-name']/text()").extract()[0].strip()
        ico_description = response.xpath("//div[@class='ico-description']/text()").extract()[0].strip()
        print('=================================================')
        # print('ico_icon', ico_icon)
        # print('ico_name', ico_name)
        # print('ico_category', ico_category)
        # print('ico_description', ico_description)
        item['ico_icon'] = ico_icon
        item['ico_name'] = ico_name
        item['ico_category'] = ico_category
        item['ico_description'] = ico_description

        yield item
