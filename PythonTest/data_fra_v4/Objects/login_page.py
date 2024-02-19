from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys

from data_fra_v4.Util.find_elements import locate_element
from data_fra_v4.Util.Log import log

"""
页面对象 用于存放页面对象（包含了哪些控件操作、元素定位）
"""


from data_fra.Util.find_elements import locate_element


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def switch_frame(self):
        """
        切换iframe
        """
        tmp_frame = locate_element(self.driver,'tag name','iframe')
        self.driver.switch_to.frame(tmp_frame)

    def input_username(self,username):
        locate_element(self.driver, 'name', 'email').send_keys(username)

    def input_password(self,password):
        log.info("object--输入密码")
        locate_element(self.driver, 'name', 'password').send_keys(password)


    def click_loginBtn(self):
        """
        点击登录按钮
        :return:
        """
        print("走到这了么")
        log.info('登录动作')
        locate_element(self.driver, 'id', 'dologin').click()



# if __name__ == "__main__":
#     path = "/usr/local/bin/chromedriver"
#     driver = webdriver.Chrome(executable_path=path)
#     driver.get('http://mail.163.com')
#     # driver.maximize_window()
#     # login_page = LoginPage(driver)
#     # login_page.switch_frame()
#     # login_page.input_username('fantastic2318')
#     # login_page.input_password('fantastic12306')
#     # login_page.click_loginBtn()
#     driver.get('chrome://settings/clearBrowserData')
#     driver.find_element('xpath','//settings-ui').send_keys(Keys.ENTER)
