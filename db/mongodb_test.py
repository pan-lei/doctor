#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 17:04
# @Author  : 潘磊
# @function: 测试mongodb

from datetime import datetime
from pymongo import MongoClient

# 建立数据库连接
client = MongoClient()
# client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017/')

# print(client.HOST)
# print(client.database_names())

# 获取数据库
db = client.users
#  db = client['test-database']
# print(type(db))

# 新增一条数据  insert_one()
# post = {
#     'name':'标题11',
#     'age':211,
#     'time':datetime.now()
# }
#
# obj = db.users.insert_one(post)
# print(type(obj))

# 新增多条数据   insert_many()
# postss = [
#     {'name':'one', 'age':1,'time':datetime.now() },
#     {'name':'two', 'age':2, 'time':datetime.now()},
#     {'name':'three', 'age':3, 'time':datetime.now()}
# ]
#
# objs = db.users.insert_many(postss)
# print(objs)

# 查询一条数据
# res = db.users.find_one()
# print(res['_id'])

# 查询多条数据
# res = db.users.find({'type':2.0})
# for i in res:
#     print(i['type'])

# 修改一条数据
# res = db.users.update_one({'name':'sue'}, {'$inc':{'age':10}})
# print(res.matched_count)
# print(res.modified_count)

# 修改多条数据
# res = db.users.update_many({'status':'A'},{"$inc":{'age':10}})
# print(res.matched_count)
# print(res.modified_count)

# 删除一条数据
# res = db.users.delete_one({'name':'sue'})
# print(res.deleted_count)

# 删除多条数据
res = db.users.delete_many({'status':'A'})
print(res.deleted_count)






