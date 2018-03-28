#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 下午1:24
# @Author  : lee
# @File    : view.py.py
# @Version : 1.0
# 说明: code后有'#'是测试时加的或者需要修改的code
# 用法：

# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)