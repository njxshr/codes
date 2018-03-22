#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 下午3:45
# @Author  : lee
# @File    : main.py
# @Version : 1.0
# 说明: code后有'#'是测试时加的或者需要修改的code
# 用法：调试工具

from scrapy.cmdline import execute


import sys
import os

# 获得当前目录
print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy","crawl","jobbole"])
execute(["scrapy","crawl","zhihu"])

