from urllib import parse
from urllib import request
import urllib
import requests
import threading
import queue
import time

# url_name的队列
url_name = queue.Queue(20)

# 请求的url
url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={}&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1621844420680'
# 请求头
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'
}


# 解析出url和name线程
class GET_URL_NAME(threading.Thread):
    def __init__(self, page_start, page_end):
        super(GET_URL_NAME, self).__init__()
        self.page_start = page_start
        self.page_end = page_end

    def run(self) -> None:
        for page in range(self.page_start, self.page_end):
            response = requests.get(url.format(page), headers=header)
            # 将请求的对象直接变为字典
            result = response.json()
            info_list = result["List"]
            for info in info_list:
                img_url = parse.unquote(info["sProdImgNo_8"]).replace('200', '0')
                img_name = parse.unquote(info["sProdName"]) + '.jpg'
                # print(threading.current_thread().name, img_name)
                # 用列表的形式将图片的url和名字放入队列
                url_name.put([img_name, img_url])


# 下载图片线程
class DOWN(threading.Thread):
    def run(self) -> None:
        # 暂停一秒，防止解析进程还未解析出数据导致下载进程直接结束
        time.sleep(1)
        while not url_name.empty():
            info = url_name.get()
            try:
                request.urlretrieve(info[1], 'images/' + info[0])
                print(threading.current_thread().name, info[0], ' 完成下载')
            except urllib.error.ContentTooShortError:
                print(info, ' 下载异常', threading.current_thread().name)


if __name__ == '__main__':
    # 两个线程获取图片的url
    get_url1 = GET_URL_NAME(0, 10)
    get_url2 = GET_URL_NAME(10, 20)
    get_url1.start()
    get_url2.start()

    # 五个线程去下载图片
    for i in range(8):
        download = DOWN(name='下载{}号'.format(i))
        download.start()
