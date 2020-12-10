#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 13:56
# @Author  : Zhangyp
# @File    : miss_bug_model.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from db4app import db
from common.util import today, this_month_start


class MissBugModel(db.Model):
	__bind_key__ = 'as'  # 指定数据库名
	__tablename__ = 'missbug'  # 指定数据库表名
	
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	zt_id = db.Column(db.SmallInteger)
	product = db.Column(db.SmallInteger)
	title = db.Column(db.String(255))
	missClass = db.Column(db.SmallInteger)
	missReason = db.Column(db.String(4))
	missReasonDetail = db.Column(db.String(4))
	solution = db.Column(db.String(255))
	owner = db.Column(db.String(8))
	occTime = db.Column(db.DateTime, nullable=False)
	
	def __init__(self, zt_id, product, title, missClass, missReason, missReasonDetail, solution, owner, occTime):
		self.zt_id = zt_id
		self.product = product
		self.title = title
		self.missClass = missClass
		self.missReason = missReason
		self.missReasonDetail = missReasonDetail
		self.solution = solution
		self.owner = owner
		# if occTime:
		# 	self.occTime = today
		self.occTime = occTime
	
	# 查询列表
	@classmethod
	def query_all(cls):
		return cls.query.all()
	
	# 条件查询
	@classmethod
	def query_params(cls, zt_id, product, missClass, missReason, owner, beginDate, endDate):
		
		# 如果未传时间范围默认为本月1号到当天的时间范围
		if not beginDate:
			beginDate = this_month_start
		if not endDate:
			endDate = today
		res = cls.query.filter(cls.occTime.between(beginDate, endDate))
		if zt_id:
			res = res.filter(cls.zt_id.in_(zt_id))
		if product:
			res = res.filter(cls.product.in_(product))
		if missClass:
			res = res.filter(cls.missClass.in_(missClass))
		if missReason:
			res = res.filter(cls.missReason.in_(missReason))
		if owner:
			res = res.filter(cls.product.in_(owner))
		return res.all()
	
	# 通过id查询
	@classmethod
	def query_id(cls, _id):
		return cls.query.get(_id)


if __name__ == '__main__':
	# mb = MissBugModel(1, 1, '现场低分辨率下样式显示问题', 2, '0001', '1001', '改进case设计方法，补充对应模块的case', 3)
	# bugs = MissBugModel.query.all()
	bugs2 = MissBugModel.query_id(2)
	print(bugs2)
