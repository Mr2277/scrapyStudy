# -*- coding: utf-8 -*-
import scrapy


class XhSpider(scrapy.Spider):
    name = 'xh'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://xiaohuar.com/']

    def parse(self, response):
        pass
