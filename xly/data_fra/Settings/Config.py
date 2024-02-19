# -*- coding: utf-8 -*- 
# @Time : 2023-12-17 13:55 
# @Author : kunp
# @File : Config.py 
# @Software: PyCharm
import os

BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

# print(BASE_DIR)

# ini 文件路径
eleLocationPath = os.path.join(BASE_DIR , 'Settings/elelemtn_location.ini')

# 测试数据文件
testDataPath = os.path.join(BASE_DIR , 'TestData/163mail.xlsx')

print(testDataPath)