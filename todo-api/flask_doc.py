#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 下午12:55
# @Author  : lee
# @File    : flask_doc.py
# @Version : 1.0
# 说明: code后有'#'是测试时加的或者需要修改的code
# 用法：

from flask import Flask
from flask import request
app = Flask(__name__)





@app.route('/')
def index():
    return "hello,world"


@app.route('/article/<id>')
def article(id):

    # return '您请求的参数id为：%s' % id
    return request.values

if __name__ == '__main__':
    app.debug = True  # 调试模式
    # app.run(host='0.0.0.0',port='5000') # 开启全网监听
    app.run()# 本地监听
