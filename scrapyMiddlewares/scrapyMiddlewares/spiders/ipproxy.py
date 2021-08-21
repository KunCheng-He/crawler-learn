import scrapy


class IpproxySpider(scrapy.Spider):
    name = 'ipproxy'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print(response.text)
        # 为了能够看到更改，所以我们发送多次请求
        # 同样的网址，Scrapy发现请求过以后不会再次请求
        # 所以我们设置一下dont_filter=True，这样就能够重复请求了
        yield scrapy.Request(self.start_urls[0], dont_filter=True)
