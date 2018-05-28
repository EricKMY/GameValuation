# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import scrapy
# import logging
from scrapytest import settings
from scrapytest.items import ScrapytestItem

class ScrapytestPipeline(object):
    #创建数据库连接,格式为utf8
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        if item.__class__ == ScrapytestItem:
            try:
                self.cursor.execute("""select * from steam_data where url = %s""", item["url"])
                ret = self.cursor.fetchone()
                if ret:
                    self.cursor.execute(
                        """update steam_data set name = %s,url = %s,price = %s""",
                        (item['name'],
                         item['url'],
                         item['price']))
                else:
                    self.cursor.execute(
                        """insert into steam_data(name,url,price)
                          value (%s,%s,%s)""",
                        (item['name'],
                         item['url'],
                         item['price']))
                self.connect.commit()
            except Exception as error:
                print(error)
                # self.logger.info(error)
            return item
