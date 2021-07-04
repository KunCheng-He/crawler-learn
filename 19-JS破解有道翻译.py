import requests
import time
import random
import hashlib  # 使用md5加密

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Referer': 'https://fanyi.youdao.com/?keyfrom=dict2.index',
    'Cookie': 'YOUDAO_MOBILE_ACCESS_TYPE=1; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=1523284257@60.12.58.56; JSESSIONID=abcDb6kMwIOwfgCZDgJOx; OUTFOX_SEARCH_USER_ID_NCOO=2124804081.0772424; ___rl__test__cookies=1624086557348'
}

# 请求的翻译服务器网址
url = "https://fanyi.youdao.com/translate_o?smartresult=dict,rule"

"""
--------------------------------------------------JS加密分析----------------------------------------------------
目标参数
i: n, 翻译的单词
from: C,
to: S,
smartresult: "dict",
client: E,
salt: r.salt,      str(时间戳) + 0~10的一个随机数
sign: r.sign,      md5加密（"fanyideskweb" + 翻译的单词 + salt + "Tbh5E8=q6U3EXe+&L[4c@"）
lts: r.ts,         str(时间戳)
bv: r.bv,          md5加密（浏览器的版本号）
doctype: "json",
version: "2.1",
keyfrom: "fanyi.web",
action: e || "FY_BY_DEFAULT"

其中的加密函数
var r = function(e) {
    var t = n.md5(navigator.appVersion),    navigator.appVersion：浏览器的版本号，是固定的，可以在浏览器的控制台查看
        r = "" + (new Date).getTime(),      这就是一个字符串类型的毫秒级时间戳
        i = r + parseInt(10 * Math.random(), 10);
    return {
        ts: r,
        bv: t,
        salt: i,
        sign: n.md5("fanyideskweb" + e + i + "Tbh5E8=q6U3EXe+&L[4c@")
    }
};
"""


if __name__ == "__main__":
    # 输入需要翻译的字符串
    text = input("输入需要翻译的字符串: ")

    # ---------------进行参数加密----------------
    # 浏览器的版本号
    browser_id  = "5.0 (X11)"
    # 时间戳
    lts = str(int(time.time() * 1000))

    salt = lts + str(random.randint(0, 10))
    sign_str = "fanyideskweb" + text + salt + "Tbh5E8=q6U3EXe+&L[4c@"
    # 进行md5加密，得到加密的值
    sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest()
    bv = hashlib.md5(browser_id.encode('utf-8')).hexdigest()
    

    # 翻译的一个表单数据
    form = {
        "i": text,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "lts": lts,
        "bv": bv,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    response = requests.post(url, headers=headers, data=form).json()
    print(response['translateResult'][0][0]["tgt"])
