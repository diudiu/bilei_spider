# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .utils.mongo_handler import MongoBase


class BileiSpiderPipeline(object):
    def __init__(self):
        self.collection = MongoBase('icodrops')

    def process_item(self, item, spider):
        ico_details = dict(item)
        ico_details.update({'spider': spider.name})
        self.collection.insert(ico_details)
        return item
