#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 15:11
# @Author  : 潘磊
# @function: 对话的初步处理，将一些客套话去除


file_name = "E:\PythonProject\doctor\dialog_test\眼科.txt"
file_input = open(file_name, 'r', encoding='utf-8')

file_input = iter(file_input)
document = ''
content = ''

for line in file_input:
    if line.startswith('http'):
        if len(document) > 0:
            print(document)
            document = ''
        else:
            continue
    else:
        if len(line.strip())>0:
            # print(document)
            if line.find('谢谢')!=-1 or line.find('不客气')!=-1 or line.find('关注')!=-1 \
                    or line.find('祝你')!=-1 or line.find('不用谢')!=-1 or line.find('图片因隐私问题无法显示')!=-1 \
                    or line.find('自动回复')!=-1 or line.find('您可以给医生送“心意”哦')!=-1:
                continue
            else:
                document += line
                # document += '\n'

