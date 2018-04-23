#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 15:55
# @Author  : 潘磊
# @function:

from mongoengine import *
from mongoengine.context_managers import switch_collection

from db.problems import Problem
from db.dialog import Dialog



class DB(object):
    def __init__(self,db_name):
        connect(db_name)

    def add_problem_one(self,data, col_name):
        doctor_name = data.split('#')[0]
        hospital = data.split('#')[1]
        date = data.split('#')[2]
        url = data.split('#')[3]
        problem_obj = Problem(
            doctor = doctor_name,
            hospital = hospital,
            date = date,
            url = url
        )
        # 这里是对 集合 Collection 进行选择
        with switch_collection(Problem, col_name):
            return problem_obj.save()

    def add_dialog_one(self, uurl,ddialog, col_name):
        save_url = uurl
        save_dialog = ddialog
        dialog_obj = Dialog(
            url = save_url,
            dialog = save_dialog
        )
        # 这里是对 集合 Collection 进行选择
        with switch_collection(Dialog, col_name):
            return dialog_obj.save()


if __name__ == '__main__':
    obj = DB('problem').add_problem_one('测试')
