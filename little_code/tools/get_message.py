#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/19 上午10:06
# @Author  : lee
# @File    : get_message.py
# @Version : 1.0
# 说明: code后有'#'是测试时加的或者需要修改的code
# 用法：

from kazoo.client import KazooClient
import logging
import base64
import rsa
logging.basicConfig()
privfile = open('rsa_private_key.pem','r')
with open('rsa_private_key.pem','r') as f:   # 读取本地的私钥
    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())

zk = KazooClient(hosts='172.18.xx.xx:xxx')  # 172.18.xx.xx:xxzookeeper地址端口
zk.start()
if zk.exists("/lambda/global"):  # /lambda/global配置文件目录
    print ("OK")
    mes = (zk.get('/lambda/global')[0]) # 取元组元素第一个
    mes = base64.b64decode(mes) # base64解码
    message = rsa.decrypt(mes, privkey).decode()
    message = base64.b64decode(message) # base64解码
    print(message)
else:
    print ("not exists.")

zk.stop()  # 停止使用zk
