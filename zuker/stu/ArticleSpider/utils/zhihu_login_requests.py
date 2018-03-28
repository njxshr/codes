#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 下午9:13
# @Author  : lee
# @File    : zhihu_login_requests.py
# @Version : 1.0
# 说明: code后有'#'是测试时加的或者需要修改的code
# 用法：

import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re
agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0"
header = {
    "HOST":"www.zhihu.com",
    "Referer":"https://www.zhihu.com",
    "User-Agent":agent
}
def get_xsrf():
    response = requests.get("https://www.zhihu.com",headers=header)
    print(response.text)

def zhihu_login(account,password):
    # 知乎登录
    if re.match("^1\d{10}",account):
        print('手机号码或者邮箱登录')
        post_url = "https://www.zhihu.com/login/phone_num"
        post_new_url = 'https://www.zhihu.com/api/v3/oauth/sign_in'
        post_data = {
            "_xsrf":"",
            "phone_num":account,
            "password":password
        }

# get_xsrf()