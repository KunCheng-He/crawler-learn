import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',

}

response = requests.get("https://www.v2ex.com", headers=headers)
print(response.status_code)

"""
需要魔法上网，本程序暂不完整
"""