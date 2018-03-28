#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 上午8:39
# @Author  : lee
# @File    : test.py
# @Version : 1.0
# 说明: code后有'#'是测试时加的或者需要修改的code
# 用法：
import sys
import os
# print(os.getcwd())
sys.path.append('../')
# sys.path.append(os.getcwd())
for i in sys.path:
    print(i)

from zuker.stu.ArticleSpider.items import ZhihuAnswerItem,ZhihuQuestionItem
# from ArticleSpider.items import ZhihuQuestionItem, ZhihuAnswerItem
