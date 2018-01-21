#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 下午2:29
# @Author  : lee
# @File    : md5转换.py
# @Version : 1.0
# 说明: code后有'#'是测试时加的或者需要修改的code
# 用法：

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
    # 需要判断是url是否是Unicode 用到 isinstance函数
    if isinstance(url,str):
        url =url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

if __name__ == "__main__":
    # 测试
    print(get_md5("www.sohu.com".encode("utf-8")))