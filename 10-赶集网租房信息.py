import requests
import re


if __name__ == '__main__':
    url = 'https://nb.58.com/chuzu/'
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'
    }

    response = requests.get(url, headers=header)
    text = response.text
    houses = re.findall(r"""
        <li.*?house-cell.*?<a.*?strongbox.*?>(.*?)</a>  # 房源标题
        .*?<p.*?room.*?>(.*?)</p>  # 户型大小
        .*?money.*?strongbox.*?>(.*?</b>.*?)</div>  # 价格
    """, text, re.VERBOSE|re.DOTALL)
    with open('赶集网租房信息.csv', 'a', encoding='utf-8') as f:
        f.write("房源信息,户型大小,价格\n")
        for i in houses:
            f.write('{},{},{}\n'.format(
                re.sub(r'\n| ', '', i[0]),
                re.sub(r' |&nbsp;|\n', '', i[1]),
                re.sub(r'</b>', '', i[2])
            ))
    print("爬取完成...")
