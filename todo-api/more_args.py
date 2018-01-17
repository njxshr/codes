#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 上午9:19
# @Author  : lee
# @File    : more_args.py
# @Version : 1.0
# 说明: code后有'#'是测试时加的或者需要修改的code
# 用法：
import json
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

from flask import request

@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'hello' + request.args.get('name')
    else:
        return 'Hello John Doe'

@app.route('/get',methods=['GET','POST'])
def postdata():
  #do some
  data = request.args
  json_dumps = json.dumps(data)
  print(data)
  print(json_dumps)
  return json_dumps

if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port='5000')
