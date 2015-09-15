# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# -*- coding:utf-8 -*-

# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IPProxyItem(scrapy.Item):

    """
    Fields

    IP
    PORT
    匿名度
    类型
    get/post支持
    位置
    响应速度
    最后验证时间
    """
    ip = scrapy.Field()
    port = scrapy.Field()
    anonymous = scrapy.Field()
    protocol = scrapy.Field()
    method = scrapy.Field()
    location = scrapy.Field()
    resp_time = scrapy.Field()
    verified_at = scrapy.Field()
