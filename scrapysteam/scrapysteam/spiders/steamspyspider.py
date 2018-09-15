# coding:utf-8
import scrapy
from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapysteam.items import ScrapySteamItem
import re

class SteamSpider(CrawlSpider):
    name = 'steamspyspider'
    allowed_domains = ['steamspy.com']
    rules = [
       Rule(LxmlLinkExtractor(allow = (r'steamspy.com/app/')),
            callback='parse_item')
    ]

    def start_requests(self):
        # self.rank = 0
        #range為頁數範圍
        for i in range(9, 10):
            # self.rank = i
            if i < 10:
                url = "https://steamspy.com/year/200" + str(i)
            else:
                url = "https://steamspy.com/year/20" + str(i)
            yield Request(url=url, callback=self.parse)
           

    # 不要使用parse，會覆蓋掉crawlspider本身的parse
    def parse_item(self, response):
        item = ScrapySteamItem()
        # item['name'] = response.url
        item['name'] = response.xpath('//div[contains(@class, "p-r-30")]//div//h3//text()').extract()
        item['url'] = response.url
        item['sell'] = response.xpath('//div[@class="p-r-30"]//text()[.="Owners"]/following::text()[string-length()>0][1]').extract()
        item['price'] = response.xpath('//div[@class="p-r-30"]//text()[.="Price:"]/following::text()[string-length()>0][1]').extract()
        item['tag'] = '!!'.join(response.xpath('//a[starts-with(@href, "/tag/")]//text()').extract())
        item['language'] = '!!'.join(response.xpath('//a[starts-with(@href, "/language/")]//text()').extract())
        item['date'] = response.xpath('//div[@class="p-r-30"]//text()[.="Release date"]/following::text()[string-length()>0][1]').extract()
        # item['sysReqMin'] = '!!'.join(response.xpath('//div[contains(@class, "game_area_sys_req_leftCol")]//text()').extract())
        # item['sysReqRec'] = '!!'.join(response.xpath('//div[contains(@class, "game_area_sys_req_rightCol")]//text()').extract())
        # item['introduction'] = ''.join(response.xpath('//div[@class="img-responsive"]//following::text()[string-length()>0][1]').extract())
        # item['about'] = ''.join(response.xpath('//div[contains(@class, "game_area_description")]//text()').extract())
        # item['sell'] = '2'
        # item['price'] = "s"
        # item['tag'] = "s"
        # item['language'] = "s"
        # item['date'] = "s"
        item['sysReqMin'] = "s"
        item['sysReqRec'] = "s"
        item['introduction'] = "s"
        item['about'] = "s"
        yield item

# /html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/p[1]/strong[13]
# /html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/p[1]/text()[36]
# : 1,000,000&nbsp;..&nbsp;2,000,000
# /html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/p[1]/text()[36]
# /html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/p[1]/strong[13]
# /html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/p[1]/a[22]