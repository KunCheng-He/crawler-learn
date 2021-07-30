import scrapy
from scrapy import linkextractors
from scrapy import item
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from .. items import ImagedownloadItem


class ZcoolSpiderSpider(CrawlSpider):
    name = 'zcool_spider'
    allowed_domains = ['zcool.com.cn', 'img.zcool.cn']
    start_urls = ['https://www.zcool.com.cn/home?p=1#tab_anchor']

    rules = {
        # 翻页的规则
        Rule(LinkExtractor(allow=".*p=\d*#tab_anchor"), follow=True),
        # 每个页面中的详情页面
        Rule(LinkExtractor(allow=".*work/.*=\.html"), follow=False, callback="parse_detail")
    }

    def parse_detail(self, response):
        title = response.xpath("//h2/text()").get().strip()
        image_list = response.xpath("//div[@class='work-show-box mt-40 js-work-content']//img/@src").getall()
        item = ImagedownloadItem(title=title, image_urls=image_list)
        yield item
