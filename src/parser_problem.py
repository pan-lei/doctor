#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/30 13:46
# @Author  : 潘磊
# @function: 根据获取到的问题 url ，得到关于病情的对话

import re
from bs4 import BeautifulSoup
import urllib.parse as up

class ProblemParser(object):
    def parseProblem(self, name, url, html_cont):
        if url is None or html_cont is None:
            return
        soup = BeautifulSoup(
            html_cont,  # 网页源代码
            'html.parser',  # 解析器
            from_encoding="gb18030"
        )
        # print(html_cont)
        self._get_dialog_content(name, url, soup)  # 由 问题url 获取 对话

    def _get_dialog_content(self, name, url, soup):
        file_name = ''.join(['E:/PythonProject/doctor/dialog/', name, '.txt'])
        # print(file_name)
        fo = open(file_name, 'a', encoding='utf-8')
        nodes = soup.find('div', class_="problem-detail-wrap").find_all('p')
        # print(nodes)
        # num = 0
        fo.write(url)
        for node in nodes:
            dic = node.attrs  # dic = {'class': ['paragraph-detail', 'right', 'blue']}
            # 存在问题，因为dic是一个字典类型，但在这里直接用dic['class']却无法获取其value值
            # 只能用下面这种折中的方法
            # key = 'class'     # 这样也不行
            # print(dic[key])
            # 这样才可以
            for i in dic:  # i = 'class'
                if dic[i][1] == 'right':
                    print('患者说:' + node.get_text().strip())
                    fo.write('患者说:' + node.get_text().strip() + '\n')
                elif dic[i][1] == 'left':
                    print('医生说:' + node.get_text().strip())
                    fo.write('医生说:' + node.get_text().strip() + '\n')
                else:
                    print('------无对话------')
        fo.write('\n')
        fo.close()
