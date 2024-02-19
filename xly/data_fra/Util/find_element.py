# -*- coding: utf-8 -*- 
# @Time : 2023-12-10 15:25 
# @Author : kunp
# @File : find_element.py 
# @Software: PyCharm

from selenium.webdriver.support.wait import WebDriverWait


def locate_element(driver, find_type, expression):
    '''
    查找控件元素
    '''
    try:
        element = WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=find_type, value= expression))
        return element
    except Exception as e:
        raise e


'''
page object
po + 三层架构
对象层 Ojbects：用于存放页面对象（包含了空间的操作）
逻辑层 Modules： 用于存放一些 封装好了的功能模块  登录，登出。。。
业务层/脚本层Scripts：真正的测试用例 
'''