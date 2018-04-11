#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 10:04
# @Author  : 潘磊


class UrlManager(object):

    def __init__(self):
        '''
        维护两个set集合，一个保存未访问过的url，一个保存已经访问过的url
        '''
        self.new_urls = set()                   # 保存root_url
        self.new_department_urls = set()        # 保存科室的url
        self.new_problem_urls = set()           # 保存问题的url
        self.old_urls = set()

    # 保存root_url
    def add_new_url(self, url):
        '''
        :向url过滤器中加入新的url
        '''
        # print("进入add_new_url函数")
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        # print(self.new_urls)

    # 保存department_urls
    def add_new_department_url(self, url):
        if url is None:
            return
        if url not in self.new_department_urls and url not in self.old_urls:
            self.new_department_urls.add(url)

    # 批量添加department_urls
    def add_new_department_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_department_url(url)

    # 保存problem_urls
    def add_new_problem_url(self, url):
        if url is None:
            return
        if url not in self.new_problem_urls and url not in self.old_urls:
            self.new_problem_urls.add(url)

    def add_new_problem_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_problem_url(url)

    def has_new_url(self):
        '''
        :判断url管理器中是否还存在新的url
        '''
        return len(self.new_urls) != 0

    def has_new_department_url(self):
        '''
        :判断url管理器中是否还存在新的new_department_url
        '''
        return len(self.new_department_urls) != 0

    def has_new_problem_url(self):
        '''
        :判断url管理器中是否还存在新的new_problem_url
        '''
        return len(self.new_problem_urls) != 0

    def get_new_url(self):
        '''
        :从url管理器中获取root_url
        '''
        # print("进入get_new_url(self)函数")
        new_url = self.new_urls.pop()           # pop方法会返回一个url，并从new_urls中删除此url
        self.old_urls.add(new_url)
        return new_url

    def get_new_department_url(self):
        '''
        :从url管理器中获取新的department_url
        '''
        new_url = self.new_department_urls.pop()           # pop方法会返回一个url，并从new_urls中删除此url
        self.old_urls.add(new_url)
        return new_url

    def get_new_problem_url(self):
        '''
        :从url管理器中获取新的problem_url
        '''
        # print("进入get_new_url(self)函数")
        new_url = self.new_problem_urls.pop()           # pop方法会返回一个url，并从new_urls中删除此url
        self.old_urls.add(new_url)
        return new_url
