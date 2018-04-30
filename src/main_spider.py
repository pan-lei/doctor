#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 13:01
# @Author  : 潘磊
# @function: 主程序

'''
    实现功能：
    大致流程：
    注意问题：
    存在问题：
'''

import os
import time

from spider_test import url_manager, html_downloder
from src import parser_root, parser_department, parser_page, \
    parser_problem,db_operation,dialog_initial_extraction,set_number

class Spider(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()                        # url管理器
        self.downloader = html_downloder.HtmlDownloader()           # 网页下载器
        self.parserRoot = parser_root.HtmlParser()                  # root网页解析器，获取到科室url的入口url，也就是第一页
        self.parserDepartment = parser_department.HtmlParser()      # department网页解析器,获取到问题url
        self.parserPage = parser_page.PageParser()                  # department第一页的解析，获取前30页
        self.parserProblem = parser_problem.ProblemParser()         # url的解析
        self.dbOperation = db_operation.DBOperation()               # problem相关信息保存
        self.dialog_initial_extraction = dialog_initial_extraction.DialogInitial()  # 对话的初步处理，将一些客套话去除
        self.number = set_number.SetNumber()                    # 设置编号

    # 根据url 获取到每个科室的 入口url
    def craw_root(self, root_url):
        # count = 1
        self.urls.add_new_url(root_url)                 # 向url管理器中添加初始的入口url

        # 对root_url进行解析
        if self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()                       # 从url管理器中获取新的url
                print("root_url = {}".format(new_url))
                html_cont = self.downloader.download(new_url)           # 对新的url下载其网页源代码
                self.parserRoot.parseRoot(new_url, html_cont)           # 利用解析器进行解析

            except:
                print("爬取失败")

    # 获取 每个科室 1-30 页的url
    def craw_department_page(self):
        # 获取第一页的url
        fr = open('E:\PythonProject\doctor\\root\department_urls_root.txt', 'r', encoding='utf-8')
        fr_iter = iter(fr)
        for line in fr_iter:
            # 皮肤病科#https://www.chunyuyisheng.com/pc/qalist/clinicno_4/
            name = line.split('#')[0]           # 科室名
            url = line.split('#')[1]            # 第一页的url
            try:
                print("Department_url = {}".format(url))
                html_cont = self.downloader.download(url)                    # 对新的url下载其网页源代码
                # print(html_cont)
                # 获取 2-30 页的的url
                self.parserPage.parsePage(name, url, html_cont)    # 利用解析器进行解析
            except:
                print("爬取失败")

        fr.close()

    # 获取所有页面上的问题url
    def get_problem_url(self):
        # 获取文件列表
        dire = os.listdir("E:\PythonProject\doctor\department")
        # dire = ['中医科.txt', '儿科.txt', '内科.txt', '口腔颌面科.txt', '外科.txt',
        #         '妇科.txt', '男科.txt', '皮肤性病科.txt', '眼科.txt', '精神心理科.txt',
        #         '耳鼻咽喉科.txt', '肿瘤及防治科.txt', '营养科.txt', '骨伤科.txt']
        for d in dire:
            # print(d)
            # print(os.path.join("E:/PythonProject/doctor/department/", d))
            name = d.split('.')[0]          # 获取文件名，用以后面的分科室保存问题url，保存在的文件名还是科室名
            # print(name)
            file = os.path.join("E:/PythonProject/doctor/department/", d)
            fr = open(file, "r", encoding='utf-8')
            fr_iter = iter(fr)
            for url in fr_iter:
                # print(url)    # 这里便是每一页的url
                try:
                    print("Department_page_url = {}".format(url))
                    html_cont = self.downloader.download(url)                       # 对新的url下载其网页源代码
                    # print(html_cont)
                    self.parserDepartment.parseDepartment(name, url, html_cont)     # 利用解析器进行解析

                except:
                    print("爬取失败")

            fr.close()

    # 获取对话内容
    def get_diglog(self):
        # 获取文件列表
        dire = os.listdir("E:\PythonProject\doctor\problem")
        # dire = ['中医科.txt', '儿科.txt', '内科.txt', '口腔颌面科.txt', '外科.txt',
        #         '妇科.txt', '男科.txt', '皮肤性病科.txt', '眼科.txt', '精神心理科.txt',
        #         '耳鼻咽喉科.txt', '肿瘤及防治科.txt', '营养科.txt', '骨伤科.txt']
        for d in dire:
            # print(d)
            # print(os.path.join("E:/PythonProject/doctor/department/", d))
            name = d.split('.')[0]  # 获取文件名，用以后面的分科室保存对话，保存在的文件名还是科室名
            # print(name)
            file = os.path.join("E:/PythonProject/doctor/problem/", d)
            fr = open(file, "r", encoding='utf-8')
            fr_iter = iter(fr)
            for data in fr_iter:
                # print(url)    # 这里便是每一个问题的url
                doctor_name = data.split('#')[0]
                hospital = data.split('#')[1]
                date = data.split('#')[2]
                url = data.split('#')[3]
                try:
                    # print("Problem_url = {0},name={1}, hopital={2},date={3}".format(url,doctor_name,hospital,date))
                    print("Problem_url = {}".format(url))  # 这里便是每一个问题的url
                    html_cont = self.downloader.download_problem(url)               # 对新的url下载其网页源代码
                    # print(html_cont)
                    self.parserProblem.parseProblem(name, url, html_cont)           # 利用解析器进行解析
                    time.sleep(3)
                except:
                    print("爬取失败")

            fr.close()
            time.sleep(3)

    # problem相关信息保存
    def save_problem(self):
        self.dbOperation.save_problems()

    # dialog相关信息保存
    def save_dialog(self):
        self.dbOperation.save_dialog()

    # 初步过滤对话的无效信息
    def dialog_initial(self):
        self.dialog_initial_extraction.dialog_initial_extraction()

    # 设置编号
    def set_number(self):
        self.number.number_set()


if __name__ == '__main__':
    root_url = "https://www.chunyuyisheng.com/pc/qalist/"
    spider = Spider()
    # spider.craw_root(root_url)
    # spider.craw_department_page()           # 获取前 30  页链接
    # spider.get_problem_url()                # 获取问题链接
    # spider.get_diglog()                     # 获取对话数据
    # spider.save_problem()                   # problem相关信息保存
    # spider.save_dialog()                    # dialog相关信息保存
    # spider.dialog_initial()                 # 对话的初步处理，将一些客套话去除
    spider.set_number()                     # 对对话进行编号