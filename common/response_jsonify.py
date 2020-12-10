#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 15:23
# @Author  : Zhangyp
# @File    : response_jsonify.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
"""返回的数据json序列化"""

from flask import jsonify


# 查询消息
def res_jsonify(data):
    if data:
        status = True
        msg = '请求成功，有数据返回'
    else:
        status = False
        msg = '请求成功，但无数据返回'
    return jsonify({
        'status': status,
        'data': data,
        'massage': msg
    })


# 操作消息
def opt_jsonify(msg):
    return jsonify({'massage': msg})
