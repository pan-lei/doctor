#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 13:52
# @Author  : 潘磊
# @function: 分析department url获取到 问题 url

from bs4 import BeautifulSoup
import urllib.parse as up
import re

class HtmlParser(object):
    def parseDepartment(self, name, url, html_cont):
        # print("进入parse(self, url, html_cont)函数")
        if url is None or html_cont is None:
            return
        # print(len(html_cont))
        soup = BeautifulSoup(
            html_cont,              # 网页源代码
            'html.parser',          # 解析器
            from_encoding="gb18030"
        )
        # print(html_cont)
        self._get_problem_urls(name, url, soup)         # 由 科室的url 获取

    def _get_problem_urls(self, name, url, soup):
        file_name = 'E:\PythonProject\doctor\problem\\' + name + '.txt'
        # print(file_name)
        fo = open(file_name, 'a', encoding='utf-8')
        # ''' 网页内容分析
        # <div class="hot-qa main-block">
        #
        #     <div class="hot-qa-item  first ">
        #         <div class="qa-item qa-item-ask">
        #             <a href="/pc/qa/6OqdUlIBYG4SksGSuTxmLg/" target="_blank">
        #                 <i class="ask-tag">问</i>
        #
        #                     为什么我的背上长了这么多痘痘,会挠出血
        #
        #             </a>
        #         </div>
        #         <div class="qa-item qa-item-answer">
        #             <i class="ask-tag answer-tag">答</i>
        #             你好，平时脸上长红色的痘痘...
        #         </div>
        #
        #         <div class="qa-item qa-item-doctor">
        #             <em>李朝辉</em>
        #             南宫妇幼保健院
        #         </div>
        #
        #         <span class="date">2018-03-23</span>
        #     </div>
        #
        #     <div class="hot-qa-item ">
        #         <div class="qa-item qa-item-ask">
        #             <a href="/pc/qa/qUUHRYRZy_g7q5bDIIeRGw/" target="_blank">
        #                 <i class="ask-tag">问</i>
        #
        #                     青春期毛孔粗大长痘痘怎么办
        #
        #             </a>
        #         </div>
        #         <div class="qa-item qa-item-answer">
        #             <i class="ask-tag answer-tag">答</i>
        #             用过药吗？ 有效果吗？ 什么药物 ...
        #         </div>
        #
        #         <div class="qa-item qa-item-doctor">
        #             <em>宋跃林</em>
        #             吉林省图们市人民医院
        #         </div>
        #
        #         <span class="date">2018-03-23</span>
        #     </div>
        #
        # </div>
        # '''
        nodes = soup.select(".hot-qa-item")
        for node in nodes:
            # print(node)
            new_url = node.find('a')['href']                                 # 获取<a>中的链接
            # print(new_url)
            new_url_full = up.urljoin(url, new_url)                          # 使新的链接格式进行规范
            # print(new_url_full)
            date = node.find('span').get_text()                              # 获取日期
            # print(date)
            doctor_name = node.find("em").get_text()                                # 获取名字
            # print(doctor_name)
            hospital_tag = node.find("div", class_="qa-item qa-item-doctor") # 获取医院
            # print(hospital)
            '''
            <div class="qa-item qa-item-doctor">
            <em>刘青云</em>
				开封市中医院
			</div>
            '''
            pattern = re.compile('</em>(.*?)</div>', re.S)
            hospital_str = re.findall(pattern, str(hospital_tag))
            hospital = str(hospital_str[0]).strip()
            # print(hospital)
            data = '#'.join([doctor_name, hospital, date, new_url_full])
            # print(date)
            fo.write(data)
            fo.write('\n')

        fo.close()


