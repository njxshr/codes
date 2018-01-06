#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/27 下午9:13
# @Author  : lee
# @File    : zhengzebiaodashi.py
# @Version : 1.0
# 说明: code后有'#'是测试时加的或者需要修改的code
# 用法：test
# import re
# line = "booooooooobby123"
# # if line == "bobby123":
# regex_str = ".*?(b.*? b)"
# # re.compile()
# if re.match(regex_str,line):
#     print(re.match(regex_str,line).group(1))

list = [i for i in range(1,10)]
print(list)
dict = {i : i for i in range(1,10)}
print(dict)

# print(result = 5>3?1:0)
print(1 if 5>3 else 0)
print('yes' if 3<1 else 'no')
a = '中文' if 3>1 else '日文'
print(a)
# if or 简化
n = 3
if n in [1,4,5,6] :
    print(n,'in list')
else:
    print(n,'not in list')
