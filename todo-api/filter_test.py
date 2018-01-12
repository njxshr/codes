#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 上午10:13
# @Author  : lee
# @File    : filter_test.py
# @Version : 1.0
# 说明: code后有'#'是测试时加的或者需要修改的code
# 用法：

def is_odd(n):
    return n %2 == 1

list = [1,2,3,4,5,6,7,8,9,10]

newlist = filter(is_odd,list)

print(newlist)
# filter_list = [item for item in a_filter_object]
filter_list = [item for item in newlist]
print(filter_list)
# for i in newlist:
#     print(i)
