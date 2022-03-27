# @Time : 2022/3/16 14:34
# @Author : Liang er qian
# @File : constants.py

import os

# 获取项目的路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# print(BASE_DIR  # D:/Casedemo/Pytestdemo

# 获取测试用例执行文件所在路径
CASE_DIR = os.path.join(BASE_DIR, 'testcase')
# print(CASE_DIR) D:/Casedemo/Pytestdemo\testcase

# 获取测试用例所在路径
DATA_DIR = os.path.join(BASE_DIR, "datas")
# print(DATA_DIR) D:/Casedemo/Pytestdemo\datas

# 在测试数据所在路径基础上，拿指定的excel测试文件
DATA_FILE = os.path.join(DATA_DIR, "cases.xlsx")

# log所在路径
LOG_DIR = os.path.join(BASE_DIR, "logs")
INFO_FILE = os.path.join(LOG_DIR, "info.logs")
ERROR_FILE = os.path.join(LOG_DIR, "error.logs")

# 配置文件所在路径
CON_DIR = os.path.join(BASE_DIR, "config")
CON_FILE = os.path.join(CON_DIR, "config.ini")

# 测试报告所在路径
REPORT_DIR = os.path.join(BASE_DIR, "report")
