#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 上午9:17
# @Author  : lee
# @File    : mysql_client.py
# @Version : 1.0
# 说明: code后有'#'是测试时加的或者需要修改的code
# 用法：测试mysql是否可以使用
import pymysql

# 配置信息
MYSQL_HOST = "123.207.157.19"  #
MYSQL_DBNAME = "jobbole"  #
MYSQL_USER = "lee"  #
MYSQL_PASSWORD = "123456"  #

def mysql_query():

    # 链接数据库
    db_nocstatis = pymysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DBNAME,
                                   charset="utf8")

    cursor = db_nocstatis.cursor()  # 数据库的游标
    SQL_commend = "select * from jobbole_article;"
    cursor.execute(SQL_commend)
    results = cursor.fetchall()

    f

mysql_query()