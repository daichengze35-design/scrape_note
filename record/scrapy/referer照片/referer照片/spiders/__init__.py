# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from scrapy.pipelines.images import ImagesPipeline

class pictureSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["blog.sina.com.cn"]
    start_urls = ["http://blog.sina.com.cn/s/blog_01ebcb8a0102zi2o.html?tj=1"]

    def parse(self, response):
        img_src_sel_dic = response.xpath('//*[@id="sina_keyword_ad_area2"]/div/a/img/@real_src')
        for img_src_sel in img_src_sel_dic:
            img_src = img_src_sel.get()
