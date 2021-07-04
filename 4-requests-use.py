import requests

# GET请求
# 设置一个请求头
# header = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
# }

# 添加一个请求参数
# kw = {'wd': '中国'}

# params 接收一个字典或字符串查询参数，字典类型自动转化为url编码，不再需要urlencode()
# response = requests.get("https://www.baidu.com/s", headers=header, params=kw)

# 请求的url
# print(response.url)

# 请求的编码
# print(response.encoding)

# 查询响应内容
# print(response.text)  # 返回unicode格式数据（字符串类型）
# print(response.content)  # 返回字节流数据
# print(response.content.decode('utf-8'))  # 当使用text属性时乱码可以自行指定编码方式

# Post请求
# 石墨文档登录的url
# url = 'https://shimo.im/lizard-api/auth/password/login'
# 提交的数据
# data = {
#     'mobile': '+8618788748257',
#     'password': 'byacksm89HKC'
# }
# response = requests.post(url, headers=header, data=data)
# print(response.text)


# 使用代理
# url = 'https://httpbin.org/ip'
# resp = requests.get(url)
# print(resp.text)
# # 加入代理
# proxy = {
#     'http': '112.111.217.230:9999'
# }
# response = requests.get(url, proxies=proxy)
# print(response.text)


# Cookie
# url = 'https://i.meishi.cc/'
# header = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
#     'cookie': 'BAIDU_SSP_lcr=https://www.meishij.net/; Hm_lvt_01dd6a7c493607e115255b7e72de5f40=1620293038; UM_distinctid=17940fdb143243-0537e8cfedb43b-192e1a0c-100200-17940fdb144bf; CNZZDATA1259001544=996200574-1620288841-https%3A%2F%2Fwww.meishij.net%2F|1620288841; __SessHandler=d8498cc568566a711d6f729c92f3e11b; last_update_time=1620293120; loginId=13686422; MSCookieKey=f4104ac7f9c5030a6171b8da08ab694d.13686422; Hm_lpvt_01dd6a7c493607e115255b7e72de5f40=1620293168'
# }
# response = requests.get(url, headers=header)
# print(response.text)
# print(response.cookies)  # 响应对象的cookie是一个RequestsCookieJar对象
# print(response.cookies.get_dict())  # 以字典的形式打印响应里的cookie

# 使用session共享cookie

# 美食杰登录的地址
# login_url = 'https://i.meishi.cc/login_t.php'
#
# hander = {
# 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
# }
#
# data = {
#     'username': '1097566154@qq.com',
#     'login_type': 2,
#     'password': 'wq15290884759.'
# }

# 使用session创建一个会话对象完成登录操作，登录完成后session就有了cookie信息
# 这个网站登录在2021年5月份使用的是get请求
# session = requests.session()
# session.get(login_url, headers=hander, params=data)

# 我的收藏链接
# url = 'https://i.meishi.cc/collected.php'
# response = session.get(url, headers=hander)
# print(response.text)

# SSL
response = requests.get('https://inv-veri.chinatax.gov.cn/', verify=False)
print(response.content.decode('utf-8'))
