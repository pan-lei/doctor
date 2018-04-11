#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 16:16
# @Author  : 潘磊
# @function: 代理池测试

import requests
from bs4 import BeautifulSoup
import urllib.parse as up

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").content

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

# your spider code

def getHtml():
    retry_count = 5
    proxy = get_proxy()
    print(str(proxy).split("'")[1])
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
    }
    while retry_count > 0:
        try:
            # 使用代理访问
            print('使用的代理https://{}'.format(str(proxy).split("'")[1]))
            response = requests.get('http://www.whatismyip.com.tw/', headers=headers, proxies={"https": "https://{}".format(str(proxy).split("'")[1])})
            if response.status_code != 200:
                return None
            # return response.text
        except Exception:
            print('wrong')
            retry_count -= 1
        else:
            # print(response.text)
            soup = BeautifulSoup(response.text, 'lxml')
            my_ip = soup.find('b').text
            print('成功连接' + my_ip)

getHtml()



