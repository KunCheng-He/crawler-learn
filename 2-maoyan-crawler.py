"""
猫眼票房实时爬取测试
"""

from urllib import request
import json


if __name__ == '__main__':

    url = "http://piaofang.maoyan.com/dashboard-ajax?orderType=0&uuid=5fc88787-4148-4e3f-ae3c-d5956142ec85&riskLevel=71&optimusCode=10&_token=eJxVjk8LgkAUxL%2FLOy%2BrW7rqggchCIMOiXUJD%2BufVgldWZcoou%2FekwwKHsy8HzMwTzBpDcIlcGsMCGDUpRwI2AkE4yxioc89HkSMQPXPoiAkUJrTBsSZrTknzHeLmWQIPiTgYUF%2B7MrDmzMpRqC1dhSOM3ZSX%2BSgaC%2F1Qw600r1Ty6kttTQ1LgEs9DkWUK%2BLykXt99%2FjdMxOnRrQNbt7flRpkmxVkh3iGF5v1So97w%3D%3D"
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }
    rq = request.Request(url, headers=header)
    response = request.urlopen(rq)
    # 使用decode()解码
    data_str = response.read().decode('utf-8')
    data = json.loads(data_str)
    data_list = data['movieList']['data']["list"]
    for i in data_list:
        print("名称：", i['movieInfo']['movieName'], "排场次：", i["showCount"])


"""
2021/4/23结果

名称： 名侦探柯南：绯色的子弹 排场次： 72981
名称： 我的姐姐 排场次： 60118
名称： 指环王：双塔奇兵 排场次： 35175
名称： 哥斯拉大战金刚 排场次： 44734
名称： 指环王：护戒使者 排场次： 15777
名称： 八月未央 排场次： 23859
名称： 记忆切割 排场次： 36597
名称： 歌声的翅膀 排场次： 266
名称： 平安中国之守护者 排场次： 151
名称： 西游记之再世妖王 排场次： 7447
名称： 第十一回 排场次： 3850
名称： 你好，李焕英 排场次： 3500
名称： 月照秋河 排场次： 102
名称： 空中之城 排场次： 14237
名称： 阿凡达 排场次： 1915
名称： 波斯语课 排场次： 820
名称： 六人-泰坦尼克上的中国幸存者 排场次： 1575
名称： 千顷澄碧的时代 排场次： 129
名称： 金刚川 排场次： 2516
名称： 进城记 排场次： 93
名称： 大事 排场次： 23
名称： 爱遍全球 排场次： 48
名称： 唐人街探案3 排场次： 794
名称： 百团大战 排场次： 1114
名称： 血战湘江 排场次： 209
名称： 圣山村谜局 排场次： 666
名称： 特别追踪 排场次： 16
名称： 小美人鱼的奇幻冒险 排场次： 1272
名称： 大地颂歌 排场次： 16
名称： 人潮汹涌 排场次： 412
名称： 青春之骏 排场次： 124
名称： 秀美人生 排场次： 64
名称： 寻龙传说 排场次： 205
名称： 半条棉被 排场次： 48
名称： 明天会好的 排场次： 458
名称： 一起走过 排场次： 184
名称： 小兵张嘎 排场次： 251
名称： 熊出没·狂野大陆 排场次： 261
名称： 工作细胞：细胞大作战 排场次： 395
名称： 迷雾追凶 排场次： 256
名称： 英雄儿女 排场次： 103
名称： 湘江1934·向死而生 排场次： 18
"""
