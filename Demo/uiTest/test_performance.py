import pytest
import pyautogui
import time
#from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.by import By
import execjs


class TestPerformance(object):
    #f = open("start.js", 'r', encoding='UTF-8')
    #cmd = 'node /Users/wufan/Project/pythonProject/Demo/uiTest/start.js'
    #capabilities = DesiredCapabilities.CHROME
    path = "/usr/local/bin/chromedriver"
    #driver = webdriver.Chrome(desired_capabilities=capabilities, executable_path=path)
    # driver.get("https://sso.lanhuapp.com//?redirect_to=https%3A%2F%2Flanhuapp.com%2Fboard%2F%3Ftid%3D18bb9a5d-9417-44c7-a35a-c4954416b2ed%26docId%3D4bb3bd12-00f9-40ab-a1f3-b4538c8a8e9f#/main/home")
    # time.sleep(2)
    # driver.maximize_window()  #窗口最大化
    # time.sleep(2)
    # print(driver.get_window_size())   #获取浏览器尺寸   {'height': 1020, 'width': 945}
    # #driver.set_window_size(width='1200',height='1000')
    # driver.find_element(By.XPATH, '//*[@id="nav"]/div/div/div[2]/div[1]/div[2]/div[2]/input').send_keys("18602495070")
    # driver.find_element(By.XPATH, '//*[@id="nav"]/div/div/div[2]/div[1]/div[2]/div[4]/div/img[2]').click()
    # driver.find_element(By.XPATH, '//*[@id="nav"]/div/div/div[2]/div[1]/div[2]/div[3]').click()
    # time.sleep(2)
    # driver.find_element(By.NAME, 'password').send_keys("11111111")
    # driver.find_element(By.XPATH, '//*[@id="nav"]/div/div/div[2]/div[1]/div/div[4]').click()
    # time.sleep(2)
    # driver.get("https://lanhuapp.com/board/?tid=18bb9a5d-9417-44c7-a35a-c4954416b2ed&docId=4bb3bd12-00f9-40ab-a1f3-b4538c8a8e9f")
    # time.sleep(5)
    driver.get("http://www.baidu.com")
    def setup(self):
        pyautogui.keyDown('F')
        pyautogui.keyUp('F')

    def test_move(self):
        #pyautogui.click(100, 300, button="left")
        pyautogui.click(950, 579, button="left", duration=2)
        # self.driver.execute_script(open("start.js").read())
        # for _ in range(5):
        #     pyautogui.dragTo(1533, 571, button="left", duration=1)
        #     pyautogui.dragTo(414, 595, button="left", duration=1)
        # self.driver.execute_script(open("end.js").read())
        # pyautogui.hotkey("command", "z")
        # print(type(start))
        # print(start)


    def teardown(self):
        self.driver.quit()
        pass

    # def teardown_Class(self):
    #     self.driver.quit()


# if __name__ == '__mai,n__':
#     # pytest.main(["test_action_filter_reload.py", "-v", "-s"])
#     pytest.main(["test_performance.py::TestPerformance::test_move", "-v", "-s"])