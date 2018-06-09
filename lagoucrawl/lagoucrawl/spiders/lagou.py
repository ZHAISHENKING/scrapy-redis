# -*- coding: utf-8 -*-
import scrapy
from lagoucrawl.items import LagoucrawlItem
# from scrapy_redis.spiders import RedisCrawlSpider


# 伯乐在线
# class LagouSpider(scrapy.Spider):
#     name = 'lagou'
#     allowed_domain = ['http://blog.jobbole.com/all-posts/']
#     start_urls = ['http://blog.jobbole.com/all-posts/']
#
#     def parse(self, response):
#         content = response.xpath('//*[@class="post floated-thumb"]')[:10]
#         for info in content:
#             href = info.css('a.archive-title::attr(href)')[0].extract()
#             yield scrapy.Request(href, callback=self.detail_parse)
#
#     def detail_parse(self, response):
#         title = response.xpath('//*[@class="entry-header"]/h1')[0].css('::text')[0].extract()
#         item = LagoucrawlItem()
#         item['title'] = title
#         yield item


# 腾讯新闻
class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domain = ['http://news.qq.com/']
    start_urls = ['http://news.qq.com/']

    def parse(self, response):
        content = response.xpath('//*[@class="linkto"]')[:10]
        for info in content:
            href = info.css('::attr(href)')[0].extract()
            yield scrapy.Request(href, callback=self.detail_parse)

    def detail_parse(self, response):
        title = response.xpath('//h1')[0].css('::text')[0].extract()
        item = LagoucrawlItem()
        item['title'] = title
        yield item