import scrapy
from scrapy import item
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ScrapyItem


class LywSpiderSpider(CrawlSpider):
    name = 'lyw_spider'
    allowed_domains = ['www.lieyunwang.com']
    start_urls = ['https://www.lieyunwang.com/latest/p1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/latest/p\d+\.html'), follow=True),
        Rule(LinkExtractor(allow=r'/archives/\d+'), callback='parse_item', follow=False)
    )

    def parse_item(self, response):
        title = ''.join(response.xpath("//div[@class='article-main']//h1/text()").getall()).strip()
        author = response.xpath('//div[@class="author-info"]/a[1]/text()').get()
        content = ''.join(response.xpath("//div[@class='main-text']//text()").getall()).strip()
        url = response.url
        item = ScrapyItem(title=title, author=author, content=content, url=url)
        return item
