#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 下午2:21
# @Author  : lee
# @File    : common.py
# @Version : 1.0
# 说明: code后有'#'是测试时加的或者需要修改的code
# 用法：

import hashlib

def get_md5(url):
    if isinstance(url,str):
        url =url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

if __name__ == "__main__":
    print(get_md5("http://jobbole.com".encode("utf-8")))