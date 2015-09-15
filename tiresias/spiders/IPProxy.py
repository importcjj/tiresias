# -*- coding:utf-8 -*-

import scrapy
from scrapy.http import Request
from tiresias.items import IPProxyItem


class IPProxySpider(scrapy.spiders.Spider):
    name = 'IPProxy'
    allowed_domains = ['kuaidaili.com']
    start_urls = [
        'http://www.kuaidaili.com/proxylist/1/'
    ]

    url_prefix = 'http://www.kuaidaili.com'

    def parse(self, response):
        listnav = response.xpath('//div[@id="listnav"]')[0]
        urls = listnav.xpath('ul/li/a/@href').extract()
        complete_urls = map(lambda url: self.url_prefix + url, urls)
        for c_url in complete_urls:
            yield Request(url=c_url, callback=self.parse_url)

    def parse_url(self, response):
        for tr in response.xpath('//tbody//tr'):
            item = IPProxyItem()
            item['ip'] = tr.xpath('td[1]/text()').extract()[0]
            item['port'] = tr.xpath('td[2]/text()').extract()[0]
            item['anonymous'] = tr.xpath('td[3]/text()').extract()[0]
            item['protocol'] = tr.xpath('td[4]/text()').extract()[0]
            item['method'] = tr.xpath('td[5]/text()').extract()[0]
            item['location'] = tr.xpath('td[6]/text()').extract()[0]
            item['resp_time'] = tr.xpath('td[7]/text()').extract()[0]
            item['verified_at'] = tr.xpath('td[8]/text()').extract()[0]
            yield item
