#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 13:19
# @Author  : 潘磊
# @function: 分析 root url 获取到 科室 url的第一页

from bs4 import BeautifulSoup
import urllib.parse as up

class HtmlParser(object):

    def parseRoot(self, url, html_cont):
        # print("进入parse(self, url, html_cont)函数")
        if url is None or html_cont is None:
            return
        # print(len(html_cont))
        soup = BeautifulSoup(
            html_cont,      # 网页源代码
            'html.parser',   # 解析器
            from_encoding="gb18030"
        )
        self._get_department_urls(url, soup)         # 由 根url 获取 科室的url

    def _get_department_urls(self, url, soup):
        # print("进入_get_new_urls(self, url, soup)函数")
        fo = open('E:\PythonProject\doctor\\root\department_urls_root.txt', 'w', encoding='utf-8')
        ''' 网页内容分析
        <ul class="tab-type-one first-clinic j-tab-wrap">

            <li class="tab-item cur">
                <a href="/pc/qalist/clinicno_4/">皮肤性病科</a>
            </li>

            <li class="tab-item">
                <a href="/pc/qalist/clinicno_1/">内科</a>
            </li>

        </ul>
        '''
        nodes = soup.find('ul', class_="tab-type-one first-clinic j-tab-wrap").find_all('li')
        # print(nodes)
        for node in nodes:
            # print(node)
            dep_name = node.find('a').get_text()  # 获取科室名字
            new_url = node.find('a')['href']  # 获取<a>中的链接
            # print(new_url)
            new_url_full = up.urljoin(url, new_url)  # 使新的链接格式进行规范
            # print(new_url_full)
            # print(dep_name + '#' + new_url_full)
            fo.write(dep_name + '#' + new_url_full)
            fo.write('\n')

        fo.close()
