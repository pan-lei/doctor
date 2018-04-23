#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 15:49
# @Author  : 潘磊
# @function: 结巴分词功能测试

import jieba

file_name = "E:\PythonProject\doctor\dialog_test\测试.txt"
content = open(file_name, 'rb').read()


seg_list = jieba.cut(content, cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut(content, cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式



seg_list = jieba.cut(content)  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search(content)  # 搜索引擎模式
print(", ".join(seg_list))


