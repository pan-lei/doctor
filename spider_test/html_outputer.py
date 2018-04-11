#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 10:24
# @Author  : 潘磊
# @function: 将获取的内容输出展示

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        # fo = open("output.html", mode='w',encoding='utf-8')
        # fo = open("output1.html", mode='w',encoding='utf-8')
        fo = open("E:\PythonProject\doctor\html\html2014_201_321.txt", mode='w',encoding='utf-8')
        # l0 = self.datas.pop(0)
        # print(l0)
        print(len(self.datas))
        for data in self.datas:
            fo.write(data['url'])
            fo.write("\n")
        # fr.close()
        # fo.write("<html>")
        # fo.write("<body>")
        # fo.write("<table>")
        # for data in self.datas:
        #     fo.write("<tr>")
        #     fo.write("<td>{}</td>".format(data['url']))
        #     # fo.write("<td>{}</td>".format(data['title']))
        #     # fo.write("<td>{}</td>".format(data['summary']))
        #     fo.write("</tr>")
        # fo.write("</table>")
        # fo.write("</body>")
        # fo.write("</html>")

        fo.close()

    def output_url(self, urls):
        fo = open("E:/PythonProject/nlp3/file/url2014_201_321.txt", mode='w', encoding='utf-8')
        for url in urls:
            fo.write(url)
            fo.write("\n")
        fo.close()