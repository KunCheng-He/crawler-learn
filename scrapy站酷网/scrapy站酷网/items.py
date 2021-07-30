# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImagedownloadItem(scrapy.Item):
    title = scrapy.Field()
    # 保存item上图片的链接
    image_urls = scrapy.Field()
    # 后期图片下载完成后形成image对象
    images = scrapy.Field()
