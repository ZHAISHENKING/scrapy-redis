# -*- coding: utf-8 -*-
import scrapy, time
from boss.items import BossItem
from scrapy_redis.spiders import RedisSpider


# class ZhipinSpider(RedisSpider):
#     name = 'zhipin'
#     allowed_domains = ['www.zhipin.com/']
#     start_urls = ['https://www.zhipin.com/c101210100/h_101210100/?query=python&page=1&ka=page-1']
#
#     def parse(self, response):
#
#         parent = response.css('.job-primary')
#
#         for child in parent:
#             item = BossItem()
#             href = child.css('::attr(href)')[0].extract()
#             target = child.css('::attr(target)')[0].extract()
#             lid = child.css('::attr(data-lid)')[0].extract()
#             ka = child.css('::attr(ka)')[0].extract()
#
#             try:
#                 item['url'] = 'https://www.zhipin.com{}?ka={}{}&lid={}'.format(href, ka, target, lid)
#                 item['job'] = child.css('.job-title::text')[0].extract()
#                 item['money'] = child.css('.red::text')[0].extract()
#                 item['company'] = child.css('.company-text>h3>a::text')[0].extract()
#                 item['time'] = child.css('.info-publis>p::text')[0].extract()
#                 item['workyear'] = child.css('.info-primary>p')[0].xpath('string(.)')[0].extract()
#                 item['xueli'] = child.css('.info-primary>p')[0].xpath('string(.)')[0].extract()
#                 item['people'] = child.css('.company-text>p')[0].xpath('string(.)')[0].extract()
#                 item['rongzi'] = child.css('.company-text>p')[0].xpath('string(.)')[0].extract()
#
#             except Exception as e:
#                 print(e)
#             yield scrapy.Request(item['url'], callback=self.detail_parse, meta={'meta_data':item}, dont_filter=True)
#             # time.sleep(5)
#
#     def detail_parse(self, response):
#         item = response.meta['meta_data']
#         try:
#             item['detail'] = response.css('.job-sec:nth-child(1)')[0].xpath('string(.)')[0].extract()
#             item['area'] = response.css('.location-address::text')[0].extract()
#         except Exception as e:
#             print(e)
#         yield item
#         print(item)


class ZhipinSpider(RedisSpider):
    name = 'zhipin'

    # start_urls = ['http://blog.jobbole.com/all-posts/']
    redis_key = 'zhipin:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(ZhipinSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        posts = response.css('div.post-meta')[:10]
        for post in posts:
            item = BossItem()
            item['link']=post.css('a.archive-title::attr(href)').extract_first()
            item['name'] =post.css('a.archive-title::text').extract_first()
            print(item)
            yield item
