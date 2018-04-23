#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 17:15
# @Author  : 潘磊
# @function: 分块读取文件操作，一次读取一个会话

file_name = "E:\PythonProject\doctor\dialog_test\眼科.txt"
print(file_name)
file_input = open(file_name, 'r', encoding='utf-8')

content = ''
file_input = iter(file_input)
for line in file_input:
    # print(line)
    if line.startswith('http'):
        if len(content)>0:
            print(content)
            content = ''
            print('------------------------')
        continue
    else:
        if len(line.strip())>0:
            content += line

if len(content.strip())>0:
    print(content)