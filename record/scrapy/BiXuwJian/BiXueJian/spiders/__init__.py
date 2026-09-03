# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from BiXueJian.items import BixuejianItem

class zhangjieming (scrapy.Spider):
    name = "zhangjieming"
    allowed_domains = ["5000yan.com"]
    start_urls = ["https://bixuejian.5000yan.com/"]

    def parse(self,response):
        Li = response.xpath('//*[@id="main-content"]/section/div/ul/li')
        for list_ditail in Li:
            title = list_ditail.xpath('./a/text()').get()
            item = BixuejianItem()
            item["title"] = title
            yield item