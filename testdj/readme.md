# 环境
- python:基于conda的python2.7
- 数据库：mysql 5.5.59
- django:1.9.5
- 查询版本
```
# 1 mysql版本
# 登录mysql后输入 :
select version();
# 2 django版本
进入python的交互环境
import django
# 回车后报错说明没有安装django pip install django==1.95
print(django.get_version())
```

#### 环境安装1.0
#### 在conda上安装python2.7
> conda create --name python27_hades python=2.7
#### 名称

> python27_hades
#### 激活 python27_hades

> activate python27_hades # for Windows
> source activate python27_hades # for Linux & Mac

#### 安装相关
-  查看当前环境下已安装的包
conda list

-  查看某个指定环境的已安装包
conda list -n python27_hades

-  查找package信息
conda search numpy

- 安装package
conda install -n python27_hades numpy
- 如果不用-n指定环境名称，则被安装在当前活跃环境
-  也可以通过-c指定通过某个channel安装

-  更新package
conda update -n python27_hades numpy

-  删除package
conda remove -n python27_hades numpy

