# coding:utf-8
import scrapy
from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapysteam.items import ScrapySteamItem
import re

class TopSeller2017Spider(CrawlSpider):
    name = 'topseller2017spider'
    allowed_domains = ['store.steampowered.com']
    start_urls = [
        'https://store.steampowered.com/sale/2017_best_sellers/'
    ]
    rules = [
       Rule(LxmlLinkExtractor(allow = (r'store.steampowered.com/app/\d+/\w+/\W\w\w\w\W')),
            callback='parse_item')
    ]

    # 不要使用parse，會覆蓋掉crawlspider本身的parse
    def parse_item(self, response):
        item = ScrapySteamItem()
        item['name'] = response.xpath('//div[contains(@class, "apphub_AppName")]//text()').extract()
        item['url'] = response.url
        item['price'] = ''.join(response.xpath('//div[contains(@class, "discount_original_price") or contains(@class, "game_purchase_price price")]//text()').extract())
        item['tag'] = ''.join(response.xpath('//div[contains(@class, "glance_tags popular_tags")]//text()').extract())
        item['language'] = ''.join(response.xpath('//td[contains(@class, "ellipsis")]//text()').extract())
        item['date'] = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " date ")]//text()').extract()
        item['sysReqMin'] = '!!'.join(response.xpath('//div[contains(@class, "game_area_sys_req_leftCol")]//text()').extract())
        item['sysReqRec'] = '!!'.join(response.xpath('//div[contains(@class, "game_area_sys_req_rightCol")]//text()').extract())
        item['introduction'] = ''.join(response.xpath('//div[contains(@class, "game_description_snippet")]//text()').extract())
        item['about'] = ''.join(response.xpath('//div[contains(@class, "game_area_description")]//text()').extract())
        yield item
