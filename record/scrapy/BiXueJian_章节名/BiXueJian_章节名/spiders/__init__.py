# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from BiXueJian_章节名.items import BixuejianItem

class zhangjieming (scrapy.Spider):
    name = "zhangjieming"
    allowed_domains = ["5000yan.com"]
    start_urls = ["https://bixuejian.5000yan.com/"]

    def parse(self,response):
        Li = response.xpath('/html/body/div[@class="container mt-md-2"]/div[@class="row custom-row"]/div[@class="col-md-9  gx-2"]/div[@class="p-2 my-2 bg-white rounded"]/ul/li')
        for list_ditail in Li:
            url_detail = list_ditail.xpath('./a/@href').get()
            yield scrapy.Request(url=url_detail, callback=self.parse_detail)
    def parse_detail(self,response):
        title = response.xpath('/html/head/title/text()').get()
        title = title.removesuffix(" - 《碧血剑》")
        item = BixuejianItem()
        item["title"] = title
        yield item