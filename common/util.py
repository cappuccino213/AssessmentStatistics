#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 11:07
# @Author  : Zhangyp
# @File    : util.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from datetime import timedelta
from datetime import datetime

"""日期处理相关"""

now = datetime.now()

# 今天
today = now

# 本月第一天和最后一天
this_month_start = datetime(now.year, now.month, 1)
this_month_end = datetime(now.year, now.month + 1, 1) - timedelta(days=1)
"""其他时间可参考
https://blog.csdn.net/xuezhangjun0121/article/details/105778739?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~sobaiduend~default-1-105778739.nonecase&utm_term=python%20%E8%8E%B7%E5%8F%96%E6%9C%AC%E6%9C%88%E7%AC%AC%E4%B8%80%E5%A4%A9&spm=1000.2123.3001.4430
"""
