import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys, DesiredCapabilities
from selenium.webdriver.common import keys
import selenium
from data_fra_v4.Modules.Login import LoginAction
from data_fra_v4.Util.Log import log
import ddt   # unittest 第三方包 数据驱动参数化

testdata = [
    {'username': 'fantastic2318', 'password': 'fantastic12306'},
    {'username': 'fantastic2319', 'password': 'fantastic12306'}
]


@ddt.ddt
class Login_Test(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print('基于类级别的方法')
    #     """
    #             前置操作打开浏览器 访问网页
    #             :return:
    #     """
    #     path = "/usr/local/bin/chromedriver"
    #     log.info("setUP 睡10秒")
    #     time.sleep(10)
    #     cls.driver = webdriver.Chrome(executable_path=path)
    #     cls.driver.get('http://mail.163.com')
    #     cls.driver.maximize_window()

    def setUp(self):
        """
        前置操作打开浏览器 访问网页
        :return:
        """
        path = "/usr/local/bin/chromedriver"
        # capabilities = DesiredCapabilities.CHROME
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.get('http://mail.163.com')
        self.driver.maximize_window()


    def tearDown(self):
        """
        后者操作 关闭浏览器
        :return:
        """
        # self.driver.get('chrome://settings/clearBrowserData')
        # self.driver.find_element('xpath', '//settings-ui').send_keys(Keys.ENTER)
        pass
        # log.info("等待30s--1")
        # time.sleep(30)
        #log.info(self.driver.get_log('browser'))
        # log.info("等待30s--2")
        # time.sleep(30)
        #log.info(self.driver.get_log('driver'))
        #self.driver.get_log('driver')
        #self.driver.quit()

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print('基于类级别后置')
    #     time.sleep(10)
    #     cls.driver.close()

    @ddt.data(*testdata)
    def test_login(self, testdata):
        """
        测试用例方法 登录
        :return:
        """
        log.info(testdata)
        username = testdata['username']
        password = testdata['password']
        log.info("V1测试用例 数据驱动")
        loginAction = LoginAction()
        log.info("---脚本登录---")
        loginAction.login(self.driver, username, password)
        time.sleep(5)
        self.assertIn("fantastic2318", self.driver.page_source)


if __name__ == "__main__":
    unittest.main() # 测试当前类当中以Test开头的方法
