from lxml import etree
import requests
import time


# 请求头信息
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}


def get_detail_url():
    """
    获取详情页面的url，拼接完成后返回一个完整的url列表
    """
    # 首页地址
    url_index = "https://www.guazi.com/wenzhou/buy/"
    response = requests.get(url_index, headers=header)
    text = response.text
    html = etree.HTML(text)
    print(text)
    # 解析出详情页面的网址
    info_link = html.xpath('//ul[@class="carlist clearfix js-top"]/li/a/@href')
    print("info_link", info_link)

    link_list = []
    url_pre = 'https://www.guazi.com'
    for i in info_link:
        link_list.append(url_pre+i)
    return link_list


if __name__ == '__main__':
    # 获取详情页面的连接列表
    link_list = get_detail_url()
    print("link_list: ", link_list)
    print("详情页面链接获取成功...")

    # 请求详情页拿到想要的数据，并写入文件进行保存，追加的方式打开
    with open('guazi_info.csv', 'a', encoding='utf-8') as f:
        f.write('车款,表显里程,排量,变速箱,全款价\n')
        for url in link_list:
            detail_html = etree.HTML(requests.get(url, headers=header).text)
            block = detail_html.xpath('//div[@class="infor-main clearfix service-open"]/div[last()]')
            title = block[0].xpath('./h1/text()')[0]
            # 将多余的/r/t替换为一个空字符，前后多余的空格使用strip()去掉
            title = title.replace(r'\r\n', '').strip()
            info = block[0].xpath('./ul/li[position()>1]/span/text()')
            price = block[0].xpath('./div[1]/div[last()]/span/text()')[0]
            f.write('{},{},{},{},{}\n'.format(title, info[0], info[1], info[2], price))
            print(title)
            time.sleep(1)

# 2021-05-11运行结果
"""
大众 迈腾 2011款 1.8TSI DSG舒适型 8万公里 1.8T 自动 5.88万
大众 朗逸 2011款 1.6L 手动品雅版 13.9万公里 1.6L 手动 2.98万
别克 凯越 2008款 1.6LE-AT 5万公里 1.6L 自动 2.00万
本田 雅阁 2008款 2.0L EX 12.49万公里 2.0L 自动 6.18万
现代ix35 2013款 2.0L 自动四驱舒适型GL 国IV 3.59万公里 2.0L 自动 8.00万
宝马3系 2011款 320i 时尚型 9.8万公里 2.0L 自动 7.68万
大众 途观 2010款 1.8TSI 自动两驱风尚版 8.7万公里 1.8T 自动 7.18万
标致408 2010款 2.0L 自动豪华版 9.34万公里 2.0L 自动 3.38万
丰田 汉兰达 2015款 2.0T 四驱豪华版 7座 4.8万公里 2.0T 自动 25.58万
奥迪Q5 2012款 2.0TFSI 进取型 12万公里 2.0T 自动 13.40万
大众 速腾 2009款 1.6L 手动时尚型真皮版 17.1万公里 1.6L 手动 2.95万
奥迪Q5 2010款 2.0TFSI 技术型 13万公里 2.0T 自动 9.20万
福特 翼虎 2013款 1.6L GTDi 两驱风尚型 10.29万公里 1.6T 自动 7.38万
标致508 2013款 2.0L 两周年纪念 自动天窗经典版 10万公里 2.0L 自动 6.58万
别克 英朗 2011款 GT 1.8L 自动时尚版真皮款 13万公里 1.8L 自动 3.98万
雪佛兰 科鲁兹 2013款 1.8L SE AT 6.8万公里 1.8L 自动 4.38万
道奇 酷威 2013款 2.4L 两驱尊尚版(进口) 6.1万公里 2.4L 自动 12.20万
大众 途观 2010款 2.0TSI 自动四驱菁英版 12.35万公里 2.0T 自动 8.58万
奥迪Q5 2013款 40 TFSI 技术型 12万公里 2.0T 自动 12.98万
别克 英朗 2013款 GT 1.8L 自动时尚版 7.1万公里 1.8L 自动 5.10万
雪佛兰 科鲁兹 2013款 1.6L SL天窗版 MT 11.3万公里 1.6L 手动 2.90万
福特 蒙迪欧 2013款 2.0L GTDi200时尚型 5.6万公里 2.0T 自动 10.38万
丰田 凯美瑞 2009款 200G 豪华版 14.3万公里 2.0L 自动 6.00万
大众 途观 2012款 2.0TSI 自动四驱旗舰版 8.37万公里 2.0T 自动 8.80万
陆风X7 2015款 2.0T 全景尊贵版 7.05万公里 2.0T 自动 5.88万
丰田 卡罗拉 2007款 1.6L 自动GL 5.8万公里 1.6L 自动 4.80万
马自达6 2008款 2.0L 自动时尚型 8万公里 2.0L 自动 4.50万
宝马X3 2014款 xDrive20i X设计套装(进口) 6.7万公里 2.0T 自动 24.50万
斯巴鲁 力狮 2010款 2.5i豪华版 10.7万公里 2.5L 自动 7.80万
福特 福克斯 2011款 两厢 1.8L 自动时尚型 7.32万公里 1.8L 自动 2.99万
现代 悦动 2008款 1.6L AT GL 15.22万公里 1.6L 自动 2.58万
雪佛兰 迈锐宝 2013款 2.0L 自动经典版 10万公里 2.0L 自动 6.38万
大众CC 2010款 2.0TSI 至尊型 12.3万公里 2.0T 自动 8.98万
福特 翼搏 2013款 1.5L 手动舒适型 7.1万公里 1.5L 手动 4.48万
大众 速腾 2012款 1.6L 自动时尚型 2万公里 1.6L 自动 6.98万
大众 Passat领驭 2011款 1.8T 自动尊品型 8万公里 1.8T 自动 5.68万
大众 高尔夫 2012款 1.4TSI 自动舒适型 9.3万公里 1.4T 自动 6.18万
别克 君越 2013款 2.4L SIDI领先舒适型 5.8万公里 2.4L 自动 8.88万
大众 帕萨特 2014款 1.4TSI DSG尊荣版 5.22万公里 1.4T 自动 10.77万
福特 翼搏 2013款 1.5L 手动风尚型 1.6万公里 1.5L 手动 3.70万
"""
