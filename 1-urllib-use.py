# 和网络相关的操作都在request模块中
from urllib import request

# 基本的请求操作
# response = request.urlopen("https://www.baidu.com")

# print(response.read())
# print(response.read(10))
# print(response.readline())
# print(response.readlines())
# print(response.getcode())

# 将指定的网址内容保存到本地，可以用来下载文件
# request.urlretrieve('https://www.sogou.com', 'sogou.html')

# 编码、解码和url解析需要导入库
# from urllib import parse

# data = {'name': "Wang", 'age': 18, 'greet': "hello world"}
# qs = parse.urlencode(data)
# print(qs)

# print(parse.quote("南城义少"))
# print(parse.parse_qs(qs))

# url = 'http://www.baidu.com/index.html;user?id=S#comment'
# print(parse.urlparse(url))
# print(parse.urlsplit(url))

# header = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
# }
# response = request.Request('https://www.baidu.com', headers=header)
# rq = request.urlopen(response)
# print(rq.read())

# 没有代理设置时
url = 'https://httpbin.org/ip'
response = request.urlopen(url)
print(response.read())

# 使用代理时
# 先使用ProxyHandler，传入代理构建一个handler
handler = request.ProxyHandler({'https': '114.239.0.112:9999'})
# 使用handler构建一个opener
opener = request.build_opener(handler)
# 使用opener去发送一个请求
resp = opener.open(url)
print(resp.read())
