#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 下午6:06
# @Author  : lee
# @File    : requestss.py
# @Version : 1.0
# 说明: code后有'#'是测试时加的或者需要修改的code
# 用法：

import requests

url = 'http://10.1.144.120:5000/zabbix?name=1&age=2&comm=3'

a = requests.get(url)
print(a.text)