#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 15:49
# @Author  : 潘磊
# @function: 结巴分词功能测试

import jieba
import jieba.posseg as pseg

# file_name = "E:\PythonProject\doctor\dialog_test\测试.txt"
# content = open(file_name, 'rb').read()
#
#
# seg_list = jieba.cut(content, cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
#
# seg_list = jieba.cut(content, cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
#
#
#
# seg_list = jieba.cut(content)  # 默认是精确模式
# print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search(content)  # 搜索引擎模式
# print(", ".join(seg_list))

seg_list = pseg.cut('熬夜 过度用眼 眼睛红血丝 右眼看东西有点模糊是近视了还是假性近视 快高考了 我该用什么药怎么办（男，18岁）')
li = []
for word, flag in seg_list:
    print('("%s", "%s"),' % (word, flag),end='')
    li.append((word, flag))
print('')
print(li)