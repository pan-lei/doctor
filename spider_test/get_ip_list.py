#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/10 20:14
# @Author  : 潘磊
# @function:

import requests
from bs4 import BeautifulSoup


def get_ip_list(url, headers):
    """ 从代理网站上获取代理"""
    ip_list = []
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'lxml')
    ul_list = soup.find_all('tr', limit=20)
    print(len(ul_list))
    for i in range(2, len(ul_list)):
        line = ul_list[i].find_all('td')
        ip = line[1].text
        port = line[2].text
        address = ip + ':' + port
        ip_list.append(address)
    return ip_list


def get_proxy(aip):
    """构建格式化的单个proxies"""
    proxy_ip = 'http://' + aip
    proxy_ips = 'https://' + aip
    proxy = {'http': proxy_ip, 'https': proxy_ips}
    return proxy