#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 15:14
# @Author  : 潘磊
# @function: 诊疗事件的抽取

import sys
sys.path.append("../")

import nltk
import jieba
jieba.load_userdict('E:\PythonProject\doctor\dict\\user_dict.txt')
import jieba.posseg as pseg

jieba.del_word('右')

file_name = "E:\PythonProject\doctor\dialog_test\眼科.txt"
# print(file_name)
file_input = open(file_name, 'r', encoding='utf-8')

content = ''
file_input = iter(file_input)
document = ''
num = 1
print(num)
for line in file_input:
    if line[0:-1].isdigit():
        num = line
        continue
    if line.startswith('http'):
        if len(document) > 0:
            # print(num)
            # print(document)
            word_list = pseg.cut(document)
            li = []
            for word, flag in word_list:
                # print('("%s", "%s"),' % (word, flag),end='')
                li.append((word, flag))
            grammar = "SYMPTOM: {<n><v|z|n|d|f|m|ns|a|uj>*<n|a|ul>}"
            cp = nltk.RegexpParser(grammar)
            result = cp.parse(li)
            for tree in result.subtrees():    # 生成树的子树，包含自身
                # 过滤根树
                if tree.label() == "S":
                    continue
                # print(list(tree))
                print("症状:",end='')
                for node in list(tree):
                    print(node[0], end='')
                print()
            print(num,end='')
            # print()
            document = ''
            # document += line
        # else:
        #     document += line
    else:
        if len(line.strip())>0:
            if len(document) > 0:
                continue
            document += str(line[4:-1])
            document += '\n'

word_list = pseg.cut(document)
li = []
for word, flag in word_list:
    # print('("%s", "%s"),' % (word, flag),end='')
    li.append((word, flag))
grammar = "SYMPTOM: {<n><v|z|n|ns|a|uj>*<n|a>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(li)
for tree in result.subtrees():    # 生成树的子树，包含自身
    # 过滤根树
    if tree.label() == "S":
        continue
    # print(list(tree))
    print("症状:", end='')
    for node in list(tree):
        print(node[0], end='')
    print()
