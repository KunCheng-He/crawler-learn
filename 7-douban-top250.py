import requests
import time
from lxml import etree

# 请求头
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
}


def get_info_url():
    """
    从10页中获取出250部电影的详细信息页面的url
    :return: 返回的一个详情页面url的列表，网页中展示的引用内容也一起返回
    """

    url_list = []
    movies_quote = []
    index = 0
    url_index = "https://movie.douban.com/top250?start={}&filter="
    for i in range(10):
        url = url_index.format(index)
        print(url)
        response = requests.get(url, headers=header)
        time.sleep(1)
        html = etree.HTML(response.text)
        movies = html.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            title = movie.xpath('./div/div[@class="info"]/div[@class="hd"]/a/@href')
            url_list.append(title[0])
            quote = movie.xpath('./div/div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()')
            # 这里要作出判断，部分电影没有引用，就解析不到元素
            try:
                movies_quote.append(quote[0])
            except IndexError:
                movies_quote.append("")

        index += 25
    return url_list, movies_quote


def get_detail_info(urls):
    """
    访问详情页面，获得电影更多详细信息
    :param urls: 传入250部电影的详情页的url列表
    :return: 返回一个详细存储详细信息的列表
    """

    info_list = []
    for url in urls:
        response = requests.get(url, headers=header)
        time.sleep(1)
        html = etree.HTML(response.text)
        name = ''.join(html.xpath('//h1/span/text()'))
        print(name)
        info = html.xpath('//div[@class="subject clearfix"]/div[@id="info"]')[0]
        director = info.xpath('./span[1]/span[last()]/a/text()')[0]
        scriptwriter = '%'.join(info.xpath('./span[2]//a/text()'))
        actor = '/'.join(info.xpath('./span[3]//a/text()'))
        category = '/'.join(info.xpath('.//span[@property="v:genre"]/text()'))
        info_list.append([name, director, scriptwriter, actor, category])
    return info_list


if __name__ == '__main__':
    # 获取详情页面连接和引用信息
    urls_link, quotes = get_info_url()
    print('----------------------------------------\n')
    # 获取详情页面的电影信息
    infos = get_detail_info(urls_link)

    # 存储信息
    print('------------------------------------------\n\n开始存储...')
    with open('top250.csv', 'a', encoding='utf-8') as f:
        f.write("电影名,引用,导演,编剧,演员,类型\n")
        for i in range(250):
            f.write("{},{},{},{},{},{}\n".format(infos[i][0], quotes[i], infos[i][1], infos[i][2], infos[i][3], infos[i][4]))
    print("运行完成")
