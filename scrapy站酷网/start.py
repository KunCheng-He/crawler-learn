from scrapy import cmdline


cmdline.execute("scrapy crawl zcool_spider".split(" "))

# import os

# dir = os.path.join(os.path.dirname(__file__), "images/1")

# if not os.path.exists(dir):
#     os.mkdir(dir)
