from data_fra_v4.Objects.login_page import LoginPage
from data_fra_v4.Util.Log import log


class LoginAction:
    def __init__(self):
        print('===开始登录===')

    # 还可以设置成staticMethod
    def login(self, driver, username, password):
        """
        封装登录动作
        :param driver:
        :param username:
        :param password:
        :return:
        """
        try:
            log.info("module方法登录")
            login_page = LoginPage(driver)
            login_page.switch_frame()
            login_page.input_username(username)
            login_page.input_password(password)
            login_page.click_loginBtn()

        except Exception as e:
            raise e


# if __name__ == "__main__":
#     path = "/usr/local/bin/chromedriver"
#     driver = webdriver.Chrome(executable_path=path)
#     driver.get('http://mail.163.com')
#     driver.maximize_window()
#     loginAction = LoginAction()
#     loginAction.login(driver, 'fantastic2318', 'fantastic12306')
#     sleep(5)
#     driver.close()
