# -*- coding: utf-8 -*-
import scrapy
import time
import re
from scrapyPM25.items import Scrapypm25Item
from .utils import *
import logging
import sys
sys.path.append("..")
sys.path.append("..")
sys.path.append("..")
import db_properties

class PmspiderSpider(scrapy.Spider):
    name = 'PMSpider'
    # allowed_domains = ['pm25.in']
    # base_urls = 'http://pm25.in/'
    allowed_domains = ['www.tianqi.com']

    def __init__(self):
        super().__init__()
        self._base_urls = 'https://www.tianqi.com/air/'
        _city_eng_list = get_city_eng(db_properties.HOST, db_properties.USER, db_properties.PASSWORD, db_properties.DATABASE)
        self._urls = []
        for city_eng_name in _city_eng_list:
            self._urls.insert(0, f"{self._base_urls}{city_eng_name}")
        self.start_urls = [self._urls.pop()]

    def parse(self, response):
        self.log(response.status)


        item = Scrapypm25Item()
        city_name = response.xpath('/html/body/div[8]/div[1]/div[1]/div[1]/span[1]/text()').get()
        aqi = response.xpath('/html/body/div[8]/div[1]/div[2]/div[1]/div[2]/div[2]/text()').get()
        co = response.xpath('/html/body/div[8]/div[1]/div[2]/div[3]/div[2]/ul/li[1]/div[2]/span[1]/text()').get()
        no2 = response.xpath('/html/body/div[8]/div[1]/div[2]/div[3]/div[2]/ul/li[2]/div[2]/span[1]/text()').get()
        o3 = response.xpath('/html/body/div[8]/div[1]/div[2]/div[3]/div[2]/ul/li[3]/div[2]/span[1]/text()').get()
        pm10 = response.xpath('/html/body/div[8]/div[1]/div[2]/div[3]/div[2]/ul/li[4]/div[2]/span[1]/text()').get()
        so2 = response.xpath('/html/body/div[8]/div[1]/div[2]/div[3]/div[2]/ul/li[5]/div[2]/span[1]/text()').get()
        pm25 = response.xpath('/html/body/div[8]/div[1]/div[2]/div[3]/div[2]/ul/li[6]/div[2]/span[1]/text()').get()

        self.log('-----------------------------')
        if city_name is None:
            eng = response.url.replace(self._base_urls, "")
            self.log(eng)
            item['city_name'] = get_city_name(db_properties.HOST, db_properties.USER, db_properties.PASSWORD, db_properties.DATABASE, eng)
            item['aqi'] = 0
            item['pm25'] = 0
            item['pm10'] = 0
            item['co'] = 0
            item['no2'] = 0
            item['o3'] = 0
            # item['o38h'] = ''.join([x for x in o38h if (x.isdigit() or x=='.')])
            item['so2'] = 0

        else:
            item['city_name'] = city_name
            item['aqi'] = aqi
            item['pm25'] = pm25
            item['pm10'] = pm10
            item['co'] = co
            item['no2'] = no2
            item['o3'] = o3
            # item['o38h'] = ''.join([x for x in o38h if (x.isdigit() or x=='.')])
            item['so2'] = so2

        yield item
        if len(self._urls) > 0:
            url = self._urls.pop()
            yield scrapy.Request(url=url, callback=self.parse, errback=self.parse_err)

    def parse_err(self, failure):
        self.log(failure)
        if len(self._urls) > 0:
            url = self._urls.pop()
            return scrapy.Request(url=url, callback=self.parse, errback=self.parse_err)