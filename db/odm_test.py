#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 13:23
# @Author  : 潘磊
# @function: 学习Mongo Engine

from mongoengine import *

# 连接数据库
connect('teacher')

SEX_CHOICE = (
    ('male','男'),
    ('female','女')
)

class Grade(EmbeddedDocument):
    name = StringField(required=True)
    grade = FloatField(required=True)

# 声明一个文档
class Teacher(Document):
    ''' 教师 '''
    name = StringField(required=True, max_length=32)
    age = IntField(required=True)
    sex = StringField(required=True,choices=SEX_CHOICE)         # 指定选择的填写
    address = StringField()
    grade = ListField(EmbeddedDocumentField(Grade))             # 嵌套
    date = DateTimeField(required=True)

    meta = {
        'collection': 'teacher'         # 指定集合名称
    }


yuwen = Grade(
    name = '语文',
    grade = 90
)

shuxue = Grade(
    name = "数学",
    grade = 90
)

tec_obj= Teacher(
    name = '姓名3',
    age = 28,
    sex = 'male',
    grade = [yuwen,shuxue],
    date = '2018-03-06'
)

# 保存一个文档，根据文档名生成对应的集合名
tec_obj.save()

# 查询一条数据   根据文档名获取数据
# res = Teacher.objects.first()
# print(res.id)

# 获取多条数据
# rows = Teacher.objects.all()
# for r in rows:
#     print(r.id)

# 根据id查询
# res = Teacher.objects.filter(pk=oid).first()

# 修改一条数据,一名男生年龄增加1岁
# res = Teacher.objects.filter(sex='male').update_one(inc__age=1)

# 修改多条数据，所有男生年龄增加1岁
# res = Teacher.objects.filter(sex='male').update(inc__age=1)


# 删除一条数据
# res = Teacher.objects.filter(sex='male').first().delete()

# 删除多条数据
# res = Teacher.objects.filter(sex= 'male').delete()


