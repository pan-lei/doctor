#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 14:13
# @Author  : 潘磊
# @function: 对对话设置编号

import os


class SetNumber(object):

    def number_set(self):
        # 获取文件列表
        dire = os.listdir(r'../dialog_initial_extraction')     # .. 代表E:\PythonProject\doctor\ 这一级
        for d in dire:
            print('正在对' + d + '编号')
            file_read = os.path.join(r'../dialog_initial_extraction', d)
            file_write = os.path.join(r'../dialog_set_number', d)
            # print(file_write)
            fr = open(file_read, "r", encoding='utf-8')
            fw = open(file_write, "w", encoding='utf-8')
            fr_iter = iter(fr)
            document = ''
            num = 1

            for line in fr_iter:
                if line.startswith('http'):
                    if len(document) > 0:
                        # print(document)
                        fw.write(str(num))
                        fw.write('\n')
                        num += 1
                        fw.write(document)
                        fw.write('\n')
                        document = ''
                        document += line
                    else:
                        document += line
                else:
                    if len(line.strip()) > 0:
                        document += line
