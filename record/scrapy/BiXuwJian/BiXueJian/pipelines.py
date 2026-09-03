# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BixuejianPipeline:
    f = None
    def open_spider(self):
        self.f = open("碧血剑章节名.txt", "w", encoding="utf-8")
    def close_spider(self):
        self.f.close()
    def process_item(self, item):
        self.f.write(item["title"] + "\n")
        return item
