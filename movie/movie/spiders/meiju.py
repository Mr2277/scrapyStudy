# -*- coding: utf-8 -*-
import scrapy


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijjutt.com']
    start_urls = ['http://meijjutt.com/']

    def parse(self, response):
        pass
