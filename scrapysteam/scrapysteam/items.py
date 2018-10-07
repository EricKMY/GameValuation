# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class ScrapySteamItem(Item):
    name = Field()
    url = Field()
    sell = Field()
    price = Field()
    date = Field()
    tag = Field()
    language = Field()
    sysReqMin = Field()
    sysReqRec = Field()
    introduction = Field()
    about = Field()
    youtube = Field()
