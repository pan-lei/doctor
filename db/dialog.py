#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 16:01
# @Author  : 潘磊
# @function: 对话文档结构

from mongoengine import *

class Dialog(Document):
    url = StringField(required=True, max_length=100)
    dialog = StringField(required=True)

    meta = {
        'collection': 'dialogs'  # 指定集合名称
    }