#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 16:19
# @Author  : 潘磊
# @function: 对对话再次进行过滤，这次是句子级别的过滤

import os

from pyhanlp import *

class DialogExtraction(object):

    def dialog_extraction(self):
        # 获取文件列表
        dire = os.listdir(r'../dialog_initial_extraction')  # .. 代表E:\PythonProject\doctor\ 这一级
        for d in dire:
            print('正在深度过滤' + d)
            file_read = os.path.join(r'../dialog_initial_extraction', d)
            file_write = os.path.join(r'../dialog_extraction', d)
            # print(file_write)
            fr = open(file_read, "r", encoding='utf-8')
            fw = open(file_write, "w", encoding='utf-8')
            fr_iter = iter(fr)
            document = ''

            for line in fr_iter:
                if line.startswith('http'):
                    if len(document) > 0:
                        print(document)
                        fw.write(document)
                        fw.write('\n')
                        document = ''
                        document += line
                    else:
                        document += line
                else:
                    if len(line.strip()) > 0:
                        document += str(line[0:4])
                        # print(type(HanLP.segment(line[4:-1])))   # <class 'jpype._jclass.java.util.ArrayList'>
                        # print(HanLP.segment(line[4:-1]))   # [你好/vl, ，/w, 这种/r, 情况/n, 多长时间/n, 了/ule, ？/w]
                        for word in HanLP.segment(line[4:-1]):
                                # print(word)
                                # print(type(str(word)))
                            if str(word).split('/')[0] == '你好':
                                # print(str(word))
                                continue
                            if str(word).split('/')[0] == '，':
                                document += ' '
                                continue
                            document += str(word).split('/')[0]
                        #
                        document += '\n'

            fw.write(document)
            fr.close()
            fw.close()



te = DialogExtraction()
te.dialog_extraction()