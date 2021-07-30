# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.python import to_bytes
from scrapy import Request
import hashlib
import re


class ImageDownloadPipeline(ImagesPipeline):
    # 构造图像下载的请求，URL从item["image_urls"]中获取
    def get_media_requests(self, item, info):
        # 将照片的名称作为参数传递出去，用于设置图片的存储路径
        return [Request(x, meta={"title": item["title"]}) for x in item.get(self.images_urls_field, [])]
    
    # 设置图片存储路径及名称
    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        # 从request的meta中获取图片所属的标题
        title = request.meta["title"]
        title = re.sub(r"[\\/?\.<>\*]", '', title)
        return f'{title}/{image_guid}.jpg'
