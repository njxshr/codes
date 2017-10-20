#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/20 上午10:56
# @Author  : lee
# @File    : weeked.py
# @Version : 1.0
# 说明: code后有'#'是测试时加的或者需要修改的code
# 用法： 判断 是否是 星期5 6 7 如果是返回0 不是返回1

import datetime

def get_datetime(): # 获取当前日期和30天内的所欲日期放入list

    oneday = datetime.timedelta(days = 1)
    nowday = datetime.date.today()
    # print("今天",nowday)
    nowdays_weekday = nowday.strftime('%A')
    # print("今天的星期",nowdays_weekday)
    yesterday = nowday-oneday
    # print("昨天",yesterday)
    yesterday_weekday = yesterday.strftime('%A')
    # print("昨天的的星期",yesterday_weekday)

    # 判断是否是周末
    if yesterday_weekday == 'Friday' or yesterday_weekday == 'Saturday' or yesterday_weekday == 'Sunday':
        return 0
    else:
        # print(yesterday_weekday)
        return 1

