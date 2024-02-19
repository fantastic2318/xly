# -*- coding: utf-8 -*- 
# @Time : 2023-12-17 10:50 
# @Author : kunp
# @File : login_page.py 
# @Software: PyCharm
from selenium import webdriver

from data_fra.Util.find_element import locate_element
from data_fra.Util.read_ini import IniParaseFile


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.parse = IniParaseFile()
        self.login_options = self.parse.getSection('163mail_login')

    def switch_frame(self):
        location_type, locaction_express = self.login_options['login_page.frame'].split(':')
        tmp_frame = locate_element(self.driver, location_type, locaction_express)
        # 切换frame
        self.driver.switch_to.frame(tmp_frame)

    def input_username(self, username):
        """
        输入用户名
        """
        location_type, locaction_express = self.login_options['login_page.username'].split(':')
        locate_element(self.driver,location_type, locaction_express).send_keys(username)

    def input_password(self, password):
        """
        输入密码
        """
        location_type, locaction_express = self.login_options['login_page.password'].split(':')
        locate_element(self.driver, location_type, locaction_express).send_keys(password)

    def click_loginBtn(self):
        '''
        点击登录按钮
        '''
        location_type, locaction_express = self.login_options['login_page.loginbutton'].split(':')
        locate_element(self.driver, location_type, locaction_express).click()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://mail.163.com')
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.switch_frame()
    login_page.input_username('zhangming002')
    login_page.input_password('zmkmzmkm')