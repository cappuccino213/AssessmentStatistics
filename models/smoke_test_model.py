#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 17:04
# @Author  : Zhangyp
# @File    : smoke_test_model.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from common.util import this_month_start, today
from db4app import db
from sqlalchemy import and_


class SmokeTestModel(db.Model):
	__bind_key__ = 'as'
	__tablename__ = 'smoketest'
	
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	title = db.Column(db.String(255))
	product = db.Column(db.SmallInteger)
	project = db.Column(db.SmallInteger)
	build = db.Column(db.String(25))
	owner = db.Column(db.String(8))
	result = db.Column(db.SmallInteger)
	reason = db.Column(db.String(255))
	perpetrators = db.Column(db.String(8))
	tester = db.Column(db.String(8))
	beginDate = db.Column(db.Date)
	endDate = db.Column(db.Date)
	zt_id = db.Column(db.SmallInteger)
	
	def __init__(self, zt_id, title, product, project, build, owner, result, reason, perpetrators, tester, beginDate,
				 endDate):
		self.zt_id = zt_id
		self.title = title
		self.product = product
		self.project = project
		self.build = build
		self.owner = owner
		self.result = result
		self.reason = reason
		self.perpetrators = perpetrators
		self.tester = tester
		self.beginDate = beginDate
		self.endDate = endDate
	
	# 条件查询
	@classmethod
	def query_params(cls, product, project, build, owner,result, perpetrators, tester, beginDate, endDate):
		if not beginDate:
			beginDate = this_month_start
		if not endDate:
			endDate = today
		res = cls.query.filter(and_(cls.beginDate>=beginDate, cls.endDate<=endDate))
		if product:
			res = res.filter(cls.product.in_(product))
		if project:
			res = res.filter(cls.project.in_(project))
		if build:
			res = res.filter(cls.build.in_(build))
		if owner:
			res = res.filter(cls.owner.in_(owner))
		if result:
			res = res.filter(cls.owner.in_(result))
		if perpetrators:
			res = res.filter(cls.perpetrators.in_(perpetrators))
		if tester:
			res = res.filter(cls.tester.in_(tester))
		return res.all()
	
	# 通过id查询
	@classmethod
	def query_id(cls, _id):
		return cls.query.get(_id)


if __name__ == "__main__":
	smokes = SmokeTestModel.query_params([], [], [], [], [], [], None, None)
	# smokes = SmokeTestModel.query_id(1)
	print(smokes[0].title)
