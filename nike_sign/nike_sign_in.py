#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 下午1:07
# @Author  : lee
# @File    : nike_sign_in.py
# @Version : 1.0
# 说明: code后有'#'是测试时加的或者需要修改的code
# 用法：

PhantomJS_path = '/Users/lee/PycharmProjects/chanjet_git/lee_codes/nike_sign/phantomjs-2.1.1-macosx/bin/phantomjs'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import ProxyType
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class NikeSignIn(object):
    def __init__(self):
        pass

    def sign(self):
        dcap = dict(DesiredCapabilities.PHANTOMJS)  # 设置userAgent
        dcap['phantomjs.page.settings.userAgent'] = ('Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1')

        browser = webdriver.PhantomJS(PhantomJS_path,desired_capabilities=dcap)
        # browser.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')

        # 不使用代理代打开ip138
        # browser.get('http://2017.ip138.com/ic.asp')
        # print('1: ', browser.session_id)
        # print('2: ', browser.page_source)
        # print('3: ', browser.get_cookies())

        # 利用DesiredCapabilities(代理设置)参数值，重新打开一个sessionId，我看意思就相当于浏览器清空缓存后，加上代理重新访问一次url
        # proxy = webdriver.Proxy()
        # proxy.proxy_type = ProxyType.MANUAL
        # proxy.http_proxy = '115.238.65.98:61202'
        # 将代理设置添加到webdriver.DesiredCapabilities.PHANTOMJS中
        # proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
        browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
        # browser.get('http://2017.ip138.com/ic.asp')
        browser.get('https://m.nike.com/cn/zh_cn/?l=shop,login_register')
        # time.sleep(2)
        # browser.find_element_by_class_name('login-text').click()
        # time.sleep(2)
        # WebElementmobile = browser.find_elements("input[name=emailAddress]")
        # WebElementmobile.sendKeys('test')

        # print('1: ', browser.session_id)
        print('2: ', browser.page_source)
        # print('3: ', browser.get_cookies())
        browser.save_screenshot('nike.png')  # 下载网页截图
        # 还原为系统代理
        # proxy = webdriver.Proxy()
        # proxy.proxy_type = ProxyType.DIRECT
        # proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
        # browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
        # browser.get('http://2017.ip138.com/ic.asp')






if __name__ == '__main__':
    item = NikeSignIn()
    item.sign()

