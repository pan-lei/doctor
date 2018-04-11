#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 10:04
# @Author  : 潘磊
# @function: 爬虫主程序

from spider_test import url_manager,html_downloder,html_parser,html_outputer

class SpiderMain(object):
    '''
    实现功能：
    大致流程：
    注意问题：
    存在问题：
    '''
    # 初始化所需工具
    def __init__(self):
        self.urls = url_manager.UrlManager()                  # url管理器
        self.downloader = html_downloder.HtmlDownloader()     # 网页下载器
        self.parser = html_parser.HtmlParser()                # 网页解析器
        self.output = html_outputer.HtmlOutputer()            # 网页输出


    # 爬虫的调度程序
    def craw(self, root_url):
        # count = 1
        self.urls.add_new_url(root_url)                 # 向url管理器中添加初始的入口url

        # 对root_url进行解析
        if self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()                       # 从url管理器中获取新的url
                print("root_url = {}".format(new_url))
                html_cont = self.downloader.download(new_url)           # 对新的url下载其网页源代码
                new_urls = self.parser.parseRoot(new_url, html_cont)    # 利用解析器进行解析
                self.urls.add_new_department_urls(new_urls)             # 将新获取的url加入department_urls，这里是批量加入

            except:
                print("爬取失败")

        # 对科室的url进行解析
        while self.urls.has_new_department_url():                       # 当department_urls中有新的url时，就循环
            try:
                new_url = self.urls.get_new_department_url()            # 从url管理器中获取新的department_url
                print("Department_url = {}".format(new_url))
                html_cont = self.downloader.download(new_url)           # 对新的url下载其网页源代码
                # print(html_cont)
                new_urls = self.parser.parseDepartment(new_url, html_cont)  # 利用解析器进行解析
                self.urls.add_new_problem_urls(new_urls)                # 将新获取的url加入problem_urls,这里是批量加入

            except:
                print("爬取失败")

        # 对问题的url进行解析
        # num = 0
        while self.urls.has_new_problem_url():                              # 当problem_urls中有新的url时，就循环
            try:
                new_url = self.urls.get_new_problem_url()                   # 从url管理器中获取新的problem_url
                print("Problem_url = {}".format(new_url))
                html_cont = self.downloader.download_problem(new_url)       # 对新的url下载其网页源代码
                self.parser.parseProblem(new_url, html_cont)                # 利用解析器进行解析
                # num += 1
                # 保存对话内容

            except:
                print("爬取失败")
                # num += 1

        # self.output.output_html()                   # 将获得的数据进行输出

if __name__ == '__main__':
    root_url = "https://www.chunyuyisheng.com/pc/qalist/"
    spider = SpiderMain()
    spider.craw(root_url)