#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/27 上午11:03
# @Author  : lee
# @File    : test.py
# @Version : 1.0
# 说明: code后有'#'是测试时加的或者需要修改的code
# 用法：

# class PhantomJS_get_png:
#     def PGP(self,url):
#         # PhantomJS 引入 # # # # #
#         import sys
#         from selenium import webdriver
#         sys.path.append('/opt/tools-noc/sendcron/jira_tower/config')
#         from jira_tower import config
#         # # # # # #
#         test1 = '2'
#         print(url)
#         # diver1 = webdriver.PhantomJS(config.PhantomJS_path)
#         # diver1.get(path_url)
#
# # PhantomJS_get_png()
# class test(PhantomJS_get_png):
#     def test1(self,url):
#         PhantomJS_get_png.PGP(self,url)
#
#
# test().test1('urlrulr')

# 装饰器


# def w1(func):
#     def inner(arg):
#         print(arg,'test')
#         a = '12'
#         return func(arg)
#
#     return inner
#
# @w1
# def f1(arg):
#     print('f1')
#     a =''
#     print(a)
# f1('11')


# class FooParent:
#     def bar(self, message):
#         print(message)
#
# class FooChild(FooParent):
#     def bar(self, message):
#         FooParent.bar(self, message)
#
# FooChild().bar("hello world")


# import re
# regex_email = re.compile(r"^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$")
# regex_d = re.compile(r"\d+$")
# a = 'lizhao2cffhasdlkfjlksdajflksadjfanjet.ced'
# if regex_d.match(a):
#     print('yes')
# if regex_email.match(a):
#     print('email yes')




