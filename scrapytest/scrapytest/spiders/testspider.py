# coding:utf-8
import scrapy
from scrapy.spiders import Spider
from scrapytest.items import ScrapytestItem
import re

class TestSpider(Spider):
    name = 'testspider'
    allowed_domains = ['store.steampowered.com']
    start_urls = [
        'https://store.steampowered.com/app/810000/Manaya/'
    ]

    def parse(self, response):
        item = ScrapytestItem()
        item['name'] = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " apphub_AppName ")]//text()').extract()
        item['url'] = response.url
        item['price'] = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " discount_final_price ")]//text()').extract()
        yield item
