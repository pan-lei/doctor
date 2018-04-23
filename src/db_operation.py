#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 11:10
# @Author  : 潘磊
# @function: 保存到MongoDB数据库

import os

from db import mongodb_tool

class DBOperation(object):

    def save_problems(self):
        '''
        将获取到的问题url相关信息保存到数据库
        :return:
        '''
        # 获取文件列表
        dire = os.listdir("E:\PythonProject\doctor\problem")
        # dire = ['中医科.txt', '儿科.txt', '内科.txt', '口腔颌面科.txt', '外科.txt',
        #         '妇科.txt', '男科.txt', '皮肤性病科.txt', '眼科.txt', '精神心理科.txt',
        #         '耳鼻咽喉科.txt', '肿瘤及防治科.txt', '营养科.txt', '骨伤科.txt']
        for d in dire:
            name = d.split('.')[0]  # 获取文件名
            print(name)
            file = os.path.join("E:/PythonProject/doctor/problem/", d)
            fr = open(file, "r", encoding='utf-8')
            fr_iter = iter(fr)
            for data in fr_iter:
                # print(url)        # 这里便是每一行
                # print(name)
                res = mongodb_tool.DB('problem').add_problem_one(data=data, col_name=name)
                print(res.id)

    def save_dialog(self):
        '''
        将获取到的问题url相关信息保存到数据库
        :return:
        '''
        # 获取文件列表
        global url
        dire = os.listdir("E:\PythonProject\doctor\dialog_test")
        # dire = ['中医科.txt', '儿科.txt', '内科.txt', '口腔颌面科.txt', '外科.txt',
        #         '妇科.txt', '男科.txt', '皮肤性病科.txt', '眼科.txt', '精神心理科.txt',
        #         '耳鼻咽喉科.txt', '肿瘤及防治科.txt', '营养科.txt', '骨伤科.txt']
        for d in dire:
            name = d.split('.')[0]  # 获取文件名
            print(name)
            file = os.path.join("E:/PythonProject/doctor/dialog_test/", d)
            fr = open(file, "r", encoding='utf-8')
            fr_iter = iter(fr)
            dialog = ''
            for num,line in enumerate(fr_iter):
                if line.startswith('http'):
                    if num == 0:
                        url = line
                    else:
                        res = mongodb_tool.DB('dialog').add_dialog_one(uurl=url, ddialog=dialog, col_name=name)
                        dialog = ''
                        print(res.id)
                        url = line
                else:
                    if len(line.strip()) > 0:
                        dialog += line
            res = mongodb_tool.DB('dialog').add_dialog_one(uurl=url, ddialog=dialog, col_name=name)
            print(res.id)