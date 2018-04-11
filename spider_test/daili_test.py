#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/10 20:15
# @Author  : 潘磊
# @function:

import requests
from spider_test import get_ip_list
from bs4 import BeautifulSoup
import time
from requests import RequestException


def print_ip(proxies):
    """利用http://www.whatismyip.com.tw/显示访问的ip"""
    cookies = {
        'sc_is_visitor_unique': 'rx6392240.1508897278.298AFF0AE2624F7BC72BADF517B67AEE.2.2.2.2.2.2.1.1.1',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
    }
    url = 'http://www.whatismyip.com.tw/'
    try:
        page = requests.get(url, headers=headers, cookies=cookies, proxies=proxies)
    except RequestException as e:
        print(str(proxies) + 'is wrong')
    else:
        soup = BeautifulSoup(page.text, 'lxml')
        my_ip = soup.find('b').text
        print('成功连接' + my_ip)


def main():
    url = 'http://www.xicidaili.com/wt'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
    }
    ip_list = get_ip_list.get_ip_list(url, headers)
    print(ip_list)
    for aip in ip_list:
        proxy = get_ip_list.get_proxy(aip)
        print_ip(proxy)


if __name__ == '__main__':
    main()