# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyPipeline:
    def open_spider(self, spider):
        self.fp = open("猎云网.csv", 'w', encoding='utf-8')
        self.fp.write("标题,作者,链接,内容\n")

    def process_item(self, item, spider):
        info = dict(item)
        self.fp.write("{},{},{},{}\n".format(info["title"], info["author"], info["url"], info["content"]))
        return item
    
    def close_spider(self, spider):
        self.fp.close()
