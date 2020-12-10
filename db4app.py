#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 11:17
# @Author  : Zhangyp
# @File    : db4app.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
"""
创建Flask应用，加载配置，将app传参给SQLAlchemy
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
# 解决跨域问题
CORS(app, suports_credentials=True)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)


# 增加操作
def add_to_db(obj):
	try:
		db.session.add(obj)
		db.session.commit()
	except Exception:
		db.session.rollback()
		db.session.flush()


# 删除
def del_db(obj):
	db.session.delete(obj)
	db.session.commit()


# 提交
def commit():
	db.session.commit()
