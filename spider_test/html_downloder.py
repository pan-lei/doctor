#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 10:11
# @Author  : 潘磊
# @function:

from urllib import request
import requests

class HtmlDownloader(object):
    def get_proxy(self):
        return requests.get("http://127.0.0.1:5010/get/").content

    def delete_proxy(self, proxy):
        requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


    def download(self, url):
        '''
        下载url对应的网页
        '''
        # print("进入download(self, url)函数")
        if url is None:
            return None
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        # req = request.Request(url)
        # req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
        # response = request.urlopen(req)
        if response.status_code != 200:
            return None
        return response.text         # 返回网页源代码

    def download_problem(self, url):
        '''
        下载url对应的网页
        '''
        # print("进入download(self, url)函数")
        retry_count = 5
        proxy = self.get_proxy()
        if url is None:
            return None
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
        while retry_count > 0:
            try:
                # 使用代理访问
                print('使用的代理https://{}'.format(str(proxy)))
                response = requests.get(url, headers=headers, proxies={"https": "https://{}".format(proxy)})
                # req = request.Request(url)
                # req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
                # response = request.urlopen(req)
                if response.status_code != 200:
                    return None
                return response.text
            except Exception:
                retry_count -= 1
        # 出错5次, 删除代理池中代理
        self.delete_proxy(proxy)
        return None

