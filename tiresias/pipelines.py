# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TiresiasPipeline(object):

    def process_item(self, item, spider):
        return item


class IPProxyPipeline(object):

    def process_item(self, item, spider):
        for small_item in item:
            print small_item
        return item
