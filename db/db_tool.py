#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 10:18
# @Author  : 潘磊
# @function: 数据库工具类

from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId

class MongoDBUtil(object):
    def __init__(self):
        '''
        初始化操作
        '''
        self.client = MongoClient()

    def get_db(self, db_name):
        '''
        :param db_name: 想要获取到的数据库的名称
        :return:  获取到的数据库
        '''
        db = self.client[db_name]
        return db

    def add_one(self, db_name, col_name, data):
        '''
        将数据插入到数据库的集合中
        :param db_name:  数据库名称
        :param col_name: 集合名称
        :param data:     插入的数据
        :return:         <class 'pymongo.results.InsertOneResult'>  inserted_id
        '''
        return db_name.col_name.insert_one(data)

    def add_many(self, db_name, col_name, data):
        '''
        :param db_name:   数据库名
        :param col_name:  集合名
        :param data:      要保存的数据
        :return:          inserted_ids
        '''
        return db_name.col_name.insert_many(data)

    def get_one(self):
        pass

    def get_more(self):
        pass

    def get_from_id(self,oid):
        pass

