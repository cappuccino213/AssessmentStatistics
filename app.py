#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 9:49
# @Author  : Zhangyp
# @File    : app.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
"""关于API的所有配置"""
from flask_restful import Api
from db4app import app

# 导入视图
from resources.miss_bug import MissBug,MissBugOption
from resources.smoke_test import SmokeTest,SmokeTestOption
from resources.zt_testtask import ZTTestTask

"""创建api"""
api = Api(app)

"""注册路由"""
# 遗漏bug
api.add_resource(MissBug, '/as/missbug/query')
api.add_resource(MissBugOption, '/as/missbug/option')

# 冒烟测试
api.add_resource(SmokeTest,'/as/smoketest/query')
api.add_resource(SmokeTestOption,'/as/smoketest/option')

# 禅道测试单
api.add_resource(ZTTestTask,'/zt/testtask/query')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8089, threaded=True)