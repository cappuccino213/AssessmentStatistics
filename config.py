#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 13:35
# @Author  : Zhangyp
# @File    : config.py.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
"""数据库配置"""

# 数据库绑定
SQLALCHEMY_BINDS = {'zentao': "mysql+pymysql://test:123456@192.168.1.43:3306/zentao?charset=UTF8MB4",
					'as': "mysql+pymysql://test:123456@192.168.1.43:3306/assessmentstatistics?charset=UTF8MB4"}

# 开启sql输出到控制台
SQLALCHEMY_ECHO = True

# Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 不走ORM连接时数据库连接
DB_INFO = dict(host="192.168.1.43", user="test", password="123456", port=3306, db="zentao", chartset="UTF8")

# print(DB_INFO)
