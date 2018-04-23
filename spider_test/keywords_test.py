#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 15:52
# @Author  : 潘磊
# @function: 结巴分词关键词抽取测试

import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser

# file_name = "E:\PythonProject\doctor\dialog_test\眼科.txt"
# print(file_name)
# content = open(file_name, 'rb').read()
# tags = jieba.analyse.extract_tags(content, topK=10, withWeight=True)
# print(tags)


file_name = "E:\PythonProject\doctor\dialog_test\测试.txt"
print(file_name)
content = open(file_name, 'rb').read()
keywords = jieba.analyse.textrank(content, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
print(keywords)