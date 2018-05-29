# coding:utf-8
import scrapy
from scrapy.spiders import Spider
from scrapysteam.items import ScrapySteamItem
import re

class TestSpider(Spider):
    name = 'testspider'
    allowed_domains = ['store.steampowered.com']
    start_urls = [
        'https://store.steampowered.com/app/810000/Manaya/',
        'https://store.steampowered.com/app/837400/Fated_Kingdom/',
        'https://store.steampowered.com/app/851580/Planet_Unknown_Runner/',
        'https://store.steampowered.com/app/858410/Black_Bart/',
    ]

    def parse(self, response):
        item = ScrapySteamItem()
        item['name'] = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " apphub_AppName ")]//text()').extract()
        item['url'] = response.url
        item['price'] = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " discount_final_price ")]//text()').extract()
        yield item
