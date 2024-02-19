# -*- coding: utf-8 -*- 
# @Time : 2023-12-17 11:16 
# @Author : kunp
# @File : test_login.py 
# @Software: PyCharm
import time

from selenium import webdriver

from data_fra.Modules.Login import LoginAction
from data_fra.Objects.login_page import LoginPage
from data_fra.Settings.Config import testDataPath
from data_fra.Util.read_excel import ExcelParse


def login_test():
    '''
    测试登录功能
    '''
    try:
        # driver = webdriver.Chrome()
        # driver.get('https://mail.163.com')
        # driver.maximize_window()

        # 不借助 业务层，直接调用对象层
        # login_page = LoginPage(driver)
        # login_page.switch_frame()
        # login_page.input_username('zhangming002')
        # login_page.inpput_password('zmkmzmkm')

        # 直接调用业务层
        # login_action = LoginAction()
        # login_action.login(driver, 'zhangming002', 'zmkmzmkm')

        excel_par = ExcelParse()
        excel_par.load_workbook(testDataPath)
        excel_par.get_sheet_by_name('login')

        # 获取行数 --》 执行几次
        rows = excel_par.get_rows_nums()
        # 获取第一行的值  ['usrname', 'password']
        row1_value = excel_par.get_row_value(1)

        for i in range(2, rows+1):
            # ['zhangming002', 'paswsword'] / ['zhangming003', 'paswsword']
            row_value = excel_par.get_row_value(i)
            # 组装成字典 {'用户名': 'zhangming002', '密码': 'zmkmzmkm'}
            values = dict(zip(row1_value, row_value))
            if values['is_need_run'].lower() == 'y':
                username = values['username']
                password = values['password']

                driver = webdriver.Chrome()
                driver.get('https://mail.163.com')
                driver.maximize_window()

                login_action = LoginAction()
                login_action.login(driver, username, password)
                time.sleep(3)
                driver.quit()

    except Exception as e:
        raise e

if __name__ == '__main__':
    login_test()