# coding:utf-8
import scrapy
from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapysteam.items import ScrapySteamItem
import re

class SteamSpider(CrawlSpider):
    name = 'steamspider'
    allowed_domains = ['store.steampowered.com']
    # start_url = ['https://store.steampowered.com/games/']
    rules = [
       Rule(LxmlLinkExtractor(allow = (r'store.steampowered.com/app/\d+/\w+/\W\w\w\w\W')),
            callback='parse_item',
            follow=True)
    ]

    def start_requests(self):
        pages = []
        for i in range(1, 101):
            url = "https://store.steampowered.com/search/?sort_by=Released_DESC&tags=-1&page=" + str(i)
            yield Request(url=url, callback=self.parse)

    # 不要使用parse，會覆蓋掉crawlspider本身的parse
    def parse_item(self, response):
        item = ScrapySteamItem()
        item['name'] = response.xpath('//div[contains(@class, "apphub_AppName")]//text()').extract()
        item['url'] = response.url
        item['price'] = response.xpath('//div[contains(@class, "discount_original_price") or contains(@class, "game_purchase_price price")]//text()').extract()
        item['tag'] = ''.join(response.xpath('//div[contains(@class, "glance_tags popular_tags")]//text()').extract())
        item['language'] = ''.join(response.xpath('//td[contains(@class, "ellipsis")]//text()').extract())
        item['introduction'] = ''.join(response.xpath('//div[contains(@class, "game_description_snippet")]//text()').extract())
        item['about'] = ''.join(response.xpath('//div[contains(@class, "game_area_description")]//text()').extract())

        # print(response.url)
        yield item
