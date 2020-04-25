# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import  pymysql
import sys
import re
sys.path.append("..")
sys.path.append("..")
from db_properties import db_param

class Scrapypm25Pipeline(object):
    def __init__(self):
        self.connect=pymysql.connect(host=db_param.host,user=db_param.user,password=db_param.password,db=db_param.database,port=3306,charset="utf8")
        self.cursor=self.connect.cursor()

    def process_item(self, item: dict, spider):

        insert_sql = \
            f"insert into WeatherSystem_airquality (city_name,record_date,aqi,pm25,pm10,co,no2,o3,so2) " \
            f"VALUES(%s,now(),%s,%s,%s,%s,%s,%s,%s)"

        if re.search(r'市', item['city_name']):
            item['city_name'] = item['city_name'].replace('市','')
        self.cursor.execute(insert_sql, (item['city_name'],item['aqi'],item['pm25'],item['pm10'],
                                         item['co'],item['no2'],item['o3'],item['so2']))

        self.connect.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
