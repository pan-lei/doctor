#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 15:55
# @Author  : 潘磊
# @function:

from mongoengine import *

from db import problems



class DB(object):
    def __init__(self,db_name):
        connect(db_name)

    def add_problem_one(self,data):
        doctor_name = data.split('#')[0]
        hospital = data.split('#')[1]
        date = data.split('#')[2]
        url = data.split('#')[3]
        problem_obj = problems.Problem(
            doctor = doctor_name,
            hospital = hospital,
            date = date,
            url = url
        )
        return problem_obj.save()


if __name__ == '__main__':
    obj = DB('problem').add_problem_one('测试')
