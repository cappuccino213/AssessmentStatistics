#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 11:16
# @Author  : Zhangyp
# @File    : zt_testtask.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from flask_restful import Resource, fields, marshal, reqparse
from models.zt_testtask_model import TestTaskModel
from common.response_jsonify import res_jsonify

post_testtask_parse = reqparse.RequestParser()
post_testtask_parse.add_argument('id', type=int, help="必须为int")

testtask_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'product': fields.Integer,
	'project': fields.Integer,
	'build': fields.String,
	'owner': fields.String,
	'begin': fields.String,
	'end': fields.String,
	'status': fields.String
}


class ZTTestTask(Resource):
	
	# 获取列表
	@staticmethod
	def get():
		args = post_testtask_parse.parse_args()
		tasks = TestTaskModel.query_id(args.id)
		data = marshal(tasks, testtask_fields)
		return res_jsonify(data)
