import scrapy
from scrapy.http import request
from ..items import ScrapyItem


class GswSpiderSpider(scrapy.Spider):
    # 爬虫的名称
    name = 'gsw_spider'
    # 只爬取这个域名下的网页
    allowed_domains = ['www.gushiwen.cn']
    # 爬虫开始的页面（可以指定多个）
    start_urls = ['https://www.gushiwen.cn/default_1.aspx']

    def parse(self, response):
        # 解析数据
        title_list = response.xpath("//div[@class='sons']/div[@class='cont']/p[1]//b/text()").getall()
        author_list = response.xpath("//div[@class='sons']/div[@class='cont']/p[2]")
        text_list = response.xpath("//div[@class='sons']/div[@class='cont']/div[@class='contson']")
        
        
        for i in range(0, 10):
            title = title_list[i]
            author = ''.join(author_list[i].xpath("./a/text()").getall())
            text = ''.join(text_list[i].xpath(".//text()").getall()).replace('\n', '')
            item = ScrapyItem(title=title, author=author, text=text)
            yield item

        # 下一页的网址
        next_url = response.xpath("//div[@class='pagesright']/a[1]/@href").get()
        # 只能爬取4页，没有下一页以后直接退出
        if next_url is None:
            return None
        request = scrapy.Request(next_url)
        yield request
