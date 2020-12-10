#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 10:09
# @Author  : Zhangyp
# @File    : smoke_test.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from flask_restful import Resource, fields, marshal, reqparse

from common.response_jsonify import res_jsonify, opt_jsonify
from db4app import add_to_db, commit, del_db
from models.smoke_test_model import SmokeTestModel

# 入参解析
post_smoke_parse = reqparse.RequestParser()
post_smoke_parse.add_argument('id', type=int, help="必须为int")
post_smoke_parse.add_argument('zt_id', type=int, action='append', help="必须为int，或者int的列表")
post_smoke_parse.add_argument('title', type=str, help="必须str")
post_smoke_parse.add_argument('product', type=int, action='append', help="必须为int，或者int的列表")
post_smoke_parse.add_argument('project', type=int, action='append', help="必须为int，或者int的列表")
post_smoke_parse.add_argument('build', type=str, action='append', help="必须为string，或者str的列表")
post_smoke_parse.add_argument('owner', type=str, action='append', help="必须为str，或者str的列表")
post_smoke_parse.add_argument('result', type=str, help="必须为str")
post_smoke_parse.add_argument('reason', type=str, help="必须为str")
post_smoke_parse.add_argument('perpetrators', type=str, action='append', help="必须为string，或者str的列表")
post_smoke_parse.add_argument('tester', type=str, action='append', help="必须为str，或者str的列表")
post_smoke_parse.add_argument('beginDate', type=str, help="必须为str")
post_smoke_parse.add_argument('endDate', type=str, help="必须为str")

# 输出字段
smoke_fields = {
	'id': fields.Integer,
	'zt_id': fields.Integer,
	'product': fields.Integer,
	'project': fields.Integer,
	'title': fields.String,
	'build': fields.String,
	'owner': fields.String,
	'result': fields.String,
	'reason': fields.String,
	'perpetrators': fields.String,
	'tester': fields.String,
	'beginDate': fields.String,
	'endDate': fields.String
}


# 创建视图资源
class SmokeTest(Resource):
	
	@staticmethod
	def get():
		pass
	
	@staticmethod
	def post():
		args = post_smoke_parse.parse_args()
		smoke_tests = SmokeTestModel.query_params(args.product, args.project, args.build, args.owner, args.result,
												  args.perpetrators, args.tester, args.beginDate, args.endDate)
		data = marshal(smoke_tests, smoke_fields)
		return res_jsonify(data)


# 增删改操作
class SmokeTestOption(Resource):
	
	# 增加
	@staticmethod
	def post():
		args = post_smoke_parse.parse_args()
		add_data = SmokeTestModel(zt_id=args.zt_id, product=args.product, project=args.project, title=args.title,
								  build=args.build, owner=args.owner, result=args.result, reason=args.reason,
								  perpetrators=args.perpetrators, tester=args.tester, beginDate=args.beginDate,
								  endDate=args.endDate)
		try:
			add_to_db(add_data)
			return opt_jsonify('增加成功')
		except Exception as e:
			return opt_jsonify(str(e))
	
	@staticmethod
	def put():
		args = post_smoke_parse.parse_args()
		original_smoke = SmokeTestModel.query_id(args.id)
		original_smoke.zt_id = args.zt_id
		original_smoke.product = args.product
		original_smoke.project = args.project
		original_smoke.title = args.title
		original_smoke.build = args.build
		original_smoke.owner = args.owner
		original_smoke.result = args.result
		original_smoke.reason = args.reason
		original_smoke.perpetrators = args.perpetrators
		original_smoke.tester = args.tester
		original_smoke.beginDate = args.beginDate
		original_smoke.endDate = args.endDate
		try:
			commit()
			return opt_jsonify('修改成功')
		except Exception as e:
			return opt_jsonify(str(e))
	
	@staticmethod
	def delete():
		args = post_smoke_parse.parse_args()
		# 查询
		original_bug = SmokeTestModel.query_id(args.id)
		try:
			del_db(original_bug)
			return opt_jsonify('删除成功')
		except Exception as e:
			return opt_jsonify(str(e))
