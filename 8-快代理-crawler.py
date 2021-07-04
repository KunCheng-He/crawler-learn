from lxml import etree
import requests
import time


if __name__ == '__main__':
    url = 'https://www.kuaidaili.com/free/inha/{}'
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'
    }
    with open('快代理-ip.csv', 'a', encoding='utf-8') as f:
        f.write("IP,PORT,匿名度,类型,位置,响应速度,最后验证时间\n")
        for i in range(1, 11):
            response = requests.get(url.format(i), headers=header)
            print(response.url)
            html = etree.HTML(response.text)
            info_list = html.xpath('//table/tbody/tr')
            for info in info_list:
                IP = info.xpath('./td[1]/text()')[0]
                PORT = info.xpath('./td[2]/text()')[0]
                anonymous = info.xpath('./td[3]/text()')[0]
                Type = info.xpath('./td[4]/text()')[0]
                Position = info.xpath('./td[5]/text()')[0]
                speed = info.xpath('./td[6]/text()')[0]
                Time = info.xpath('./td[7]/text()')[0]
                f.write('{},{},{},{},{},{},{}\n'.format(IP, PORT, anonymous, Type, Position, speed, Time))
            time.sleep(1)
