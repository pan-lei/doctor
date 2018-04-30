#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 9:37
# @Author  : 潘磊
# @function: nltk测试

import sys
sys.path.append("../")

import nltk
import jieba
jieba.load_userdict('E:\PythonProject\doctor\dict\\user_dict.txt')
import jieba.posseg as pseg


# ####信息提取####
# def ie_preprocess(document):
#     sentences = nltk.sent_tokenize(document)
#     sentences = [nltk.word_tokenize(sent) for sent in sentences]
#     sentences = [nltk.pos_tag(sent) for sent in sentences]


####分块####
# [熬夜/vi,  /w, 过度/d, 用/p, 眼/n,  /w, 眼睛/n, 红血丝/nz,  /w, 右眼/n, 看/v, 东西/n, 有点/d, 模糊/a, 是/vshi, 近视/a, 了/ule, 还是/c, 假性近视/nz,  /w,
#  快/a, 高考/vn, 了/ule,  /w, 我/rr, 该/rz, 用/p, 什么药/nz, 怎么办/ryv, （/w, 男/b, ，/w, 18/m, 岁/qt, ）/w]
# sentence = [("那个", "DT"), ("小", "JJ"), ("黄", "JJ"),("狗", "NN"), ("对着", "IN"), ("那只", "DT"), ("猫", "NN"), ("叫", "VBD")]
# grammar = "NP: {<DT>?<JJ>*<NN>}"
# cp = nltk.RegexpParser(grammar)
# result = cp.parse(sentence)
# print(result)
# result.draw()
# jieba.add_word('右眼')
'''
grammar = r"""
NP: {<DT|PP\$>?<JJ>*<NN>} # chunk determiner/possessive, adjectives and nouns
{<NNP>+} # chunk sequences of proper nouns
"""
'''
# grammar = r"""
# NP: {<n><v|n|a|uj>*<n|v>}
# """
jieba.del_word('右')
jieba.del_word('肿')
# jieba.del_word('是')
# jieba.add_word('是')
# jieba.del_word('近视')
# word_list = pseg.cut('眼睛出现淡淡的虹视现象是怎么回事？3,4个星期前测过眼压是正常，散瞳检查过眼底没有问题，现在眼睛能看见淡淡的不明显的彩虹光环，分不太清颜色而且只在看离得比较近比较大的路灯能看见，台灯，头上的灯泡都看不见（男，20岁）')
word_list = pseg.cut('上眼皮之前是肿，现在是红不退，芦荟可以搽眼皮吗？是否能恢复')
li = []
for word, flag in word_list:
    # print('("%s", "%s"),' % (word, flag),end='')
    li.append((word, flag))
# [('熬夜', 'v'), (' ', 'x'), ('过度', 'n'), ('用', 'p'), ('眼', 'n'), (' ', 'x'), ('眼睛', 'n'), ('红血丝', 'n'), (' ', 'x'), ('右', 'f'), ('眼看', 'v'), ('东西', 'ns'),
# ('有点', 'n'), ('模糊', 'a'), ('是', 'v'), ('近视', 'v'), ('了', 'ul'), ('还是', 'c'), ('假性近视', 'l'), (' ', 'x'),
# ('快', 'a'), ('高考', 'v'), ('了', 'ul'), (' ', 'x'), ('我', 'r'), ('该', 'r'), ('用', 'p'), ('什么', 'r'), ('药', 'n'), ('怎么办', 'l'), ('（', 'x'), ('男', 'n'), ('，', 'x'), ('18', 'm'), ('岁', 'm'), ('）', 'x')]
grammar = "SYMPTOM: {<n><v|z|n|d|f|m|ns|a|uj>*<n|a|ul>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(li)
print(result)

# for tree in result.subtrees():
#     print(tree)
#     # 过滤根树
#     if tree.label() == "S":
#         continue
#     # print(list(tree))
#     for node in list(tree):
#         print(node[0],end='')
#     print(end=' ')
