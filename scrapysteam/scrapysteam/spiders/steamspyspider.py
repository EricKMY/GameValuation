# coding:utf-8
import scrapy
from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapysteam.items import ScrapySteamItem
from scrapy.selector import HtmlXPathSelector
import re

class SteamSpider(CrawlSpider):
    name = 'steamspyspider'
    allowed_domains = ['steamspy.com','store.steampowered.com']
    rules = [
       Rule(LxmlLinkExtractor(allow = (r'steamspy.com/app/',r'store.steampowered.com/app/\d+/\w+/\W\w\w\w\W')),
            callback='parse_item')
    ]

    def start_requests(self):
        #range為頁數範圍
        for i in range(16, 18):
            if i < 10:
                url = "https://steamspy.com/year/200" + str(i)
            else:
                url = "https://steamspy.com/year/20" + str(i)
            yield Request(url=url, callback=self.parse)
           

    # 不要使用parse，會覆蓋掉crawlspider本身的parse
    def parse_item(self, response):
        item = ScrapySteamItem()
        item['name'] = response.xpath('//div[contains(@class, "p-r-30")]//div//h3//text()').extract()
        item['url'] = response.url
        item['sell'] = response.xpath('//div[@class="p-r-30"]//text()[.="Owners"]/following::text()[string-length()>0][1]').extract()
        item['price'] = response.xpath('//div[@class="p-r-30"]//text()[.="Price:"]/following::text()[string-length()>0][1]').extract()
        item['tag'] = '!!'.join(response.xpath('//a[starts-with(@href, "/tag/")]//text()').extract())
        item['language'] = '!!'.join(response.xpath('//a[starts-with(@href, "/language/")]//text()').extract())
        item['date'] = response.xpath('//div[@class="p-r-30"]//text()[.="Release date"]/following::text()[string-length()>0][1]').extract()
        target = response.xpath('//a[contains(text(), "Store")]/@href').extract()[0]

        # hxs = HtmlXPathSelector(response)
        # response.url = hxs.select('//a[contains(text(), "Store")]/@href').extract()
        # item['sysReqMin'] = '!!'.join(response.xpath('//div[contains(@class, "game_area_sys_req_leftCol")]//text()').extract())
        # item['sysReqRec'] = '!!'.join(response.xpath('//div[contains(@class, "game_area_sys_req_rightCol")]//text()').extract())
        # item['introduction'] = ''.join(target.xpath('//div[contains(@class, "apphub_AppName")]//text()').extract())
        # item['about'] = ''.join(response.xpath('//div[contains(@class, "game_area_description")]//text()').extract())
        # item['sell'] = '2'
        # item['price'] = "s"
        # item['tag'] = "s"
        # item['language'] = "s"
        # item['date'] = "s"
        # item['sysReqMin'] = "s"
        # item['sysReqRec'] = "s"
        # item['introduction'] = response.url
        # item['about'] = "s"
        # yield item
        yield Request(target, meta={'item': item}, callback = self.parse_detail)
    
    def parse_detail(self, response):
        item = response.meta['item']
        item['sysReqMin'] = '!!'.join(response.xpath('//div[contains(@class, "game_area_sys_req_leftCol")]//text()').extract())
        item['sysReqRec'] = '!!'.join(response.xpath('//div[contains(@class, "game_area_sys_req_rightCol")]//text()').extract())
        item['introduction'] = response.xpath('//div[contains(@class, "game_description_snippet")]//text()').extract()
        item['about'] = ''.join(response.xpath('//div[contains(@class, "game_area_description")]//text()').extract())
        yield item