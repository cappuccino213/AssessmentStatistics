#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 17:04
# @Author  : Zhangyp
# @File    : miss_bug.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

"""创建视图资源"""

from flask_restful import Resource, fields, marshal, reqparse
from models.miss_bug_model import MissBugModel
from common.response_jsonify import res_jsonify, opt_jsonify
from db4app import add_to_db, commit, del_db
from common.util import today

# 入参解析
post_bug_parse = reqparse.RequestParser()
post_bug_parse.add_argument('id', type=int, help="必须为int")
post_bug_parse.add_argument('zt_id', type=int, action='append', help="必须为int，或者int的列表")
post_bug_parse.add_argument('title', type=str, help="必须str")
post_bug_parse.add_argument('product', type=int, action='append', help="必须为int，或者int的列表")
post_bug_parse.add_argument('missClass', type=int, action='append', help="必须为int，或者int的列表")
post_bug_parse.add_argument('missReason', type=str, action='append', help="必须为str，或者str的列表")
post_bug_parse.add_argument('missReasonDetail', type=str, help="必须为str")
post_bug_parse.add_argument('owner', type=str, action='append', help="必须为str，或者str的列表")
post_bug_parse.add_argument('solution', type=str, help="必须为str")
post_bug_parse.add_argument('beginDate', type=str)
post_bug_parse.add_argument('endDate', type=str)

# 字段输出
bug_fields = {
	'id': fields.Integer,
	'zt_id': fields.Integer,
	'product': fields.Integer,
	'title': fields.String,
	'missClass': fields.Integer,
	'missReason': fields.String,
	'missReasonDetail': fields.String,
	'solution': fields.String,
	'owner': fields.String,
	'occTime': fields.String
}


# 创建视图资源(查询)
class MissBug(Resource):
	
	# 获取列表
	@staticmethod
	def get():
		bugs = MissBugModel.query_all()
		data = marshal(bugs, bug_fields)
		return res_jsonify(data)
	
	# 条件查询
	@staticmethod
	def post():
		args = post_bug_parse.parse_args()  # 入参解析
		bugs = MissBugModel.query_params(args.zt_id,
										 args.product,
										 args.missClass,
										 args.missReason,
										 args.owner,
										 args.beginDate,
										 args.endDate)
		data = marshal(bugs, bug_fields)
		return res_jsonify(data)


# 增删改
class MissBugOption(Resource):
	
	# 增加
	@staticmethod
	def post():
		args = post_bug_parse.parse_args()
		bug = MissBugModel(zt_id=args.zt_id, product=args.product, title=args.title, missClass=args.missClass,
						   missReason=args.missReason, missReasonDetail=args.missReasonDetail, owner=args.owner,
						   solution=args.solution, occTime=today)
		try:
			add_to_db(bug)
			return opt_jsonify('增加成功')
		except Exception as e:
			return opt_jsonify(str(e))
	
	# 修改
	@staticmethod
	def put():
		args = post_bug_parse.parse_args()
		# 查询
		original_bug = MissBugModel.query_id(args.id)
		# 修改
		original_bug.product = args.product
		original_bug.title = args.title
		original_bug.missClass = args.missClass
		original_bug.missReason = args.missReason
		original_bug.missReasonDetail = args.missReasonDetail
		original_bug.owner = args.owner
		original_bug.solution = args.solution
		original_bug.occTime = today
		# 提交修改
		try:
			commit()
			return opt_jsonify('修改成功')
		except Exception as e:
			return opt_jsonify(str(e))
	
	# 删除
	@staticmethod
	def delete():
		args = post_bug_parse.parse_args()
		# 查询
		original_bug = MissBugModel.query_id(args.id)
		try:
			del_db(original_bug)
			return opt_jsonify('删除成功')
		except Exception as e:
			return opt_jsonify(str(e))
