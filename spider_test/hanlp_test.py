#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 10:16
# @Author  : 潘磊
# @function: 测试HanLP的功能


from pyhanlp import *

'''
print(HanLP.segment('你好，欢迎在Python中调用HanLP的API'))
for term in HanLP.segment('下雨天地面积水'):
    print('{}\t{}'.format(term.word, term.nature)) # 获取单词与词性
testCases = [
    "商品和服务",
    "结婚的和尚未结婚的确实在干扰分词啊",
    "买水果然后来世博园最后去世博会",
    "中国的首都是北京",
    "欢迎新老师生前来就餐",
    "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作",
    "随着页游兴起到现在的页游繁盛，依赖于存档进行逻辑判断的设计减少了，但这块也不能完全忽略掉。"]
for sentence in testCases: print(HanLP.segment(sentence))
# 关键词提取
document = "水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露，" \
           "根据刚刚完成了水资源管理制度的考核，有部分省接近了红线的指标，" \
           "有部分省超过红线的指标。对一些超过红线的地方，陈明忠表示，对一些取用水项目进行区域的限批，" \
           "严格地进行水资源论证和取水许可的批准。"
print(HanLP.extractKeyword(document, 2))
# 自动摘要
print(HanLP.extractSummary(document, 3))
# 依存句法分析
print(HanLP.parseDependency("徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。"))
'''
file_name = "E:\PythonProject\doctor\dialog_test\眼科.txt"
# print(file_name)
file_input = open(file_name, 'r', encoding='utf-8')

content = ''
file_input = iter(file_input)
document = ''
for line in file_input:
    if line.startswith('http'):
        if len(document) > 0:
            print(document)
            document = ''
            document += line
        else:
            document += line
    else:
        if len(line.strip())>0:
            document += str(line[0:4])
            # print(type(HanLP.segment(line[4:-1])))   # <class 'jpype._jclass.java.util.ArrayList'>
            # print(HanLP.segment(line[4:-1]))   # [你好/vl, ，/w, 这种/r, 情况/n, 多长时间/n, 了/ule, ？/w]
            for word in HanLP.segment(line[4:-1]):
            #     # print(word)
            #     # print(type(str(word)))
                if str(word).split('/')[0] == '你好':
                    # print(str(word))
                    continue
                if str(word).split('/')[0] == '，':
                    document += ' '
                    continue
                document += str(word).split('/')[0]
            #
            document += '\n'
#             print(HanLP.segment(line[4:-1]))
#
# print(document)

