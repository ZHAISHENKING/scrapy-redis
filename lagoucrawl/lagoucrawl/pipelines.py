# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.exporter import JsonItemExporter


class LagoucrawlPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonPipeline(object):
    """
    使用自带方法
    """
    def __init__(self):
        self.f = open('news.json','wb')
        self.exporter = JsonItemExporter(self.f,encoding='utf-8')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()