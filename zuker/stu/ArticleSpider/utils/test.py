#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/23 上午12:32
# @Author  : lee
# @File    : test.py
# @Version : 1.0
# 说明: code后有'#'是测试时加的或者需要修改的code
# 用法： 测试脚本 知道zhihu.js的原理

import execjs
import time

timestamp = int(time.time() * 1000)

fp = open('zhihu.js')
js = fp.read()
fp.close()
ctx = execjs.compile(js)
print(ctx.call('getSignature',timestamp))
# signature = ctx.call('getSignature', timestamp)