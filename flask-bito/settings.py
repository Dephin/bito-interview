#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : settings.py
# @Author  : dephin
# @File    : 2019-07-06

# 调试模式是否开启
DEBUG = False

SQLALCHEMY_TRACK_MODIFICATIONS = True
# session必须要设置key
SECRET_KEY='A0Zr98j/3yX R~XHH!jmN]LWX/,?RS'

# mysql数据库连接信息,这里改为自己的账号
DB_CONF = {
    'user': 'root',
    'password': '',
    'ip': 'localhost',
    'port': '3306',
    'db': 'bito_interview',
}
SQLALCHEMY_DATABASE_URI = "mysql://{user}:{password}@{ip}:{port}/{db}".format(**DB_CONF)

SQLALCHEMY_COMMIT_ON_TEARDOWN = True
