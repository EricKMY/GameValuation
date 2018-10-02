# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import scrapy
from scrapysteam import settings
from scrapysteam.items import ScrapySteamItem

class ScrapySteamPipeline(object):
    #創建數據庫連結,格式為utf8
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
        if item.__class__ == ScrapySteamItem:
            try:
                self.cursor.execute("""select * from steam_spy_2016 where url = %s""", item["url"])
                ret = self.cursor.fetchone()
                if ret:
                    self.cursor.execute(
                        """update steam_spy_2016 set name = %s,url = %s,sell = %s,price = %s,date = %s,
                        tag = %s,language = %s,sys_req_min = %s,sys_req_rec = %s,introduction = %s,about = %s""",
                        (item['name'],
                         item['url'],
                         item['sell'],
                         item['price'],
                         item['date'],
                         item['tag'],
                         item['language'],
                         item['sysReqMin'],
                         item['sysReqRec'],
                         item['introduction'],
                         item['about']))
                else:
                    self.cursor.execute(
                        """insert into steam_spy_2016(name,url,sell,price,date,tag,language,sys_req_min,sys_req_rec,introduction,about)
                          value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                        (item['name'],
                         item['url'],
                         item['sell'],
                         item['price'],
                         item['date'],
                         item['tag'],
                         item['language'],
                         item['sysReqMin'],
                         item['sysReqRec'],
                         item['introduction'],
                         item['about']))
                self.connect.commit()
            except Exception as error:
                print(error)
            return item
