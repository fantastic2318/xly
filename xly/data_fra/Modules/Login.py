# -*- coding: utf-8 -*- 
# @Time : 2023-12-17 11:09 
# @Author : kunp
# @File : Login.py 
# @Software: PyCharm
from selenium import webdriver

from data_fra.Objects.login_page import LoginPage


class LoginAction:

    def __init__(self):
       print('-----开始登录了-----')

    # @staticmethod
    def login(self, driver, username, password):
        '''
        封装登录动作
        '''
        try:
            login_page = LoginPage(driver)
            login_page.switch_frame()
            login_page.input_username(username)
            login_page.input_password(password)
            # login_page.click_loginBtn()
        except Exception as e:
            raise e

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://mail.163.com')
    driver.maximize_window()
    login_action = LoginAction()
    login_action.login(driver, 'zhangming002', 'zmkmzmkm')

