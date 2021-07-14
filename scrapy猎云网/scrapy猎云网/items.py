# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyItem(scrapy.Item):
    title = scrapy.Field()     # 文章的标题
    author = scrapy.Field()    # 文章的作者
    content = scrapy.Field()   # 文章的内容
    url = scrapy.Field()       # 文章的地址
