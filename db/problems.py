#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 16:00
# @Author  : 潘磊
# @function: 问题文档结构

from mongoengine import *

class Problem(Document):
    doctor = StringField(required=True,max_length=5)
    hospital = StringField(required=True,max_length=50)
    date = DateTimeField(required=True)
    url = StringField(required=True, max_length=100)

    meta = {
        'collection': 'problems'         # 指定集合名称
    }
