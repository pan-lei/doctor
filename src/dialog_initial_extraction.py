#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 9:47
# @Author  : 潘磊
# @function: 对话的初步处理，将一些客套话去除

import os


class DialogInitial(object):

    def dialog_initial_extraction(self):
        # 获取文件列表
        dire = os.listdir(r'../dialog')     # .. 代表E:\PythonProject\doctor\ 这一级
        for d in dire:
            print('正在初步过滤' + d)
            file_read = os.path.join(r'../dialog', d)
            file_write = os.path.join(r'../dialog_initial_extraction', d)
            # print(file_write)
            fr = open(file_read, "r", encoding='utf-8')
            fw = open(file_write, "w", encoding='utf-8')
            fr_iter = iter(fr)
            document = ''

            for line in fr_iter:
                if line.startswith('http'):
                    if len(document) > 0:
                        # print(document)
                        fw.write(document)
                        fw.write('\n')
                        document = ''
                        document += line
                    else:
                        document += line
                else:
                    if len(line.strip()) > 0:
                        # 这里有问题，不能够句子中出现这些词语就整句删除
                        if line.find('谢谢') != -1 or line.find('不客气') != -1 or line.find('关注') != -1 \
                                or line.find('祝你') != -1 or line.find('不用谢') != -1 \
                                or line.find('自动回复') != -1 or line.find('您可以给医生送“心意”哦') != -1 \
                                or line.find('晚安') != -1 or line.find('祝早日康复') != -1 or line.find('再见') != -1\
                                or line.find('Your browser does not') != -1 or line.find('｡◕‿◕｡') != -1 \
                                or line.find('^_^') != -1  or line.find('🌹🌹🌹') != -1 or line.find('祝您') != -1 \
                                or line.find('给我好评') != -1 or line.find('左下角评价') != -1 \
                                or line.find('👍👍👍') != -1 or line.find('👍👍') != -1:
                            continue
                        # 这里的处理很有灵性   or line.find('图片因隐私问题无法显示') != -1
                        if line.find('图片因隐私问题无法显示') != -1:
                            line = line[:line.find('图片因隐私问题无法显示')]
                            # print(line)
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('🙂') != -1:
                            # print(line.find('🙂'))
                            line = line[:line.find('🙂')] + line[line.find('🙂')+1:-1]
                            # print(line)
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('😊') != -1:
                            # print(line.find('😊'))
                            line = line[:line.find('😊')] + line[line.find('😊')+1:-1]
                            # print(line)
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('😁') != -1:
                            # print(line.find('😊'))
                            line = line[:line.find('😁')] + line[line.find('😁')+1:-1]
                            # print(line)
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('😓') != -1:
                            # print(line.find('😊'))
                            line = line[:line.find('😓')] + line[line.find('😓')+1:-1]
                            # print(line)
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('😞') != -1:
                            # print(line.find('😊'))
                            line = line[:line.find('😞')] + line[line.find('😞')+1:-1]
                            # print(line)
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('🙏') != -1:
                            line = line[:line.find('🙏')] + line[line.find('🙏')+1:-1]
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('👌') != -1:
                            line = line[:line.find('👌')] + line[line.find('👌')+1:-1]
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('🍀') != -1:
                            line = line[:line.find('🍀')] + line[line.find('🍀')+1:-1]
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('😂') != -1:
                            # print(line.find('😊'))
                            line = line[:line.find('😂')] + line[line.find('😂')+1:-1]
                            # print(line)
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('💝') != -1:
                            # print(line.find('😊'))
                            line = line[:line.find('💝')] + line[line.find('💝')+1:-1]
                            # print(line)
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('💓') != -1:
                            # print(line.find('😊'))
                            line = line[:line.find('💓')] + line[line.find('💓')+1:-1]
                            # print(line)
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('😢') != -1:
                            # print(line.find('😊'))
                            line = line[:line.find('😢')] + line[line.find('😢')+1:-1]
                            # print(line)
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('😭') != -1:
                            # print(line.find('😊'))
                            line = line[:line.find('😭')] + line[line.find('😭')+1:-1]
                            # print(line)
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('🆗') != -1:
                            # print(line.find('😊'))
                            line = line[:line.find('🆗')] + line[line.find('🆗')+1:-1]
                            # print(line)
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('😭') != -1:
                            # print(line.find('😊'))
                            line = line[:line.find('😭')] + line[line.find('😭')+1:-1]
                            # print(line)
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('😘') != -1:
                            # print(line.find('😊'))
                            line = line[:line.find('😘')] + line[line.find('😘')+1:-1]
                            # print(line)
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('😱') != -1:
                            line = line[:line.find('😱')] + line[line.find('😱')+1:-1]
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('😄') != -1:
                            line = line[:line.find('😄')] + line[line.find('😄')+1:-1]
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('💊') != -1:
                            line = line[:line.find('💊')] + line[line.find('💊')+1:-1]
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('🍭') != -1:
                            line = line[:line.find('🍭')] + line[line.find('🍭')+1:-1]
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('😥') != -1:
                            line = line[:line.find('😥')] + line[line.find('😥')+1:-1]
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('😔') != -1:
                            line = line[:line.find('😔')] + line[line.find('😔')+1:-1]
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('👍') != -1:
                            line = line[:line.find('👍')] + line[line.find('👍')+1:-1]
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('🏥') != -1:
                            line = line[:line.find('🏥')] + line[line.find('🏥')+1:-1]
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('😛') != -1:
                            line = line[:line.find('😛')] + line[line.find('😛')+1:-1]
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('🤝') != -1:
                            line = line[:line.find('🤝')] + line[line.find('🤝')+1:-1]
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('😳') != -1:
                            line = line[:line.find('😳')] + line[line.find('😳')+1:-1]
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('😨') != -1:
                            line = line[:line.find('😨')] + line[line.find('😨')+1:-1]
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('👆') != -1:
                            line = line[:line.find('👆')] + line[line.find('👆')+1:-1]
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        if line.find('😠') != -1:
                            line = line[:line.find('😠')] + line[line.find('😠')+1:-1]
                            if len(line.strip()) > 0:
                                document += line
                                continue
                            else:
                                continue
                        else:
                            document += line
                    # 🤯   😱   😄  💊  🍭  😥  😔 👍  🏥  😛  🤝  😳  😨  👆  😠

            fw.write(document)
            fr.close()
            fw.close()
