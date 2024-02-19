import time

from selenium import webdriver

from action_fra.Util.find_elements import locate_element, locate_elements

driver = None


def open_browser(browser_name, *args):
    """
    打开浏览器
    :param browser_name:
    :param args:
    :return:
    """
    global driver
    path = "/usr/local/bin/chromedriver"
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome(executable_path=path)
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox(executable_path=path)
    else:
        driver = webdriver.Ie(executable_path=path)


def max_window(*args):
    """
    窗口最大化
    :param args:
    :return:
    """
    try:
        driver.maximize_window()
    except Exception as e:
        raise e


def enter_url(url,*args):
    """
    输入网址
    :param url:
    :param args:
    :return:
    """
    try:
        driver.get(url)
    except Exception as e:
        raise e


def switch_frame(location_type,location_express,*args):
    """
    切换Frame
    :param location_type:
    :param location_express:
    :param args:
    :return:
    """
    try:
        i_frame = locate_element(driver, location_type, location_express)
        driver.switch_to.frame(i_frame)
    except Exception as e:
        raise e


def switch_frame_out(*args):
    """
    切至Frame外
    :param location_type:
    :param location_express:
    :param args:
    :return:
    """
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e

def input_content(location_type, location_express, input_cont,*args):
    """
    文本框输入
    :return:
    """
    try:
        print("--input_content--")
        locate_element(driver, location_type, location_express).send_keys(input_cont)
        print(locate_element(driver, location_type, location_express))
    except Exception as e:
        raise e


def click(location_type, location_express, *args):
    """
    单击操作
    :param location_type:
    :param location_express:
    :param args:
    :return:
    """
    try:
        locate_element(driver, location_type, location_express).click()
    except Exception as e:
        raise e


def assertInPagesource(content, *args):
    """
    断言是否在页面源码中
    :param content:
    :param args:
    :return:
    """
    try:
        if content in driver.page_source:
            print("you")
        else:
            print("meiyou")
    except Exception as e:
        raise e


def close_browser(*args):
    try:
        driver.quit()
    except Exception as e:
        raise e


def wait_time(test_data, *args):
    try:
        time.sleep(test_data)
    except Exception as e:
        raise e


def refresh_page(*args):
    try:
        driver.refresh()
    except Exception as e:
        raise e


def input_content_list(location_type, location_express, value, *args):
    """
    location_type，location_express返回列表、选择列表中某个值定位控件
    :param location_type:
    :param location_express:
    :param value:
    :param args:
    :return:
    """
    try:
        location_express, index = location_express.split(",")
        locate_elements(driver, location_type, location_express)[2].send_keys("测试")
    except Exception as e:
        raise e


# if __name__ == "__main__":
#     open_browser("chrome")
#     max_window()
#     enter_url("http://mail.163.com")
#     switch_frame("tag name", "iframe")
#     input_content("name", "email",'fantastic2318')
#     input_content("name", "password", 'fantastic12306')
#     click("id", "dologin")
#     time.sleep(10)
#     refresh_page()
#     #assertInPagesource("fantastic2318")
#     click('xpath', "/html/body/div[1]/nav/div[1]/ul/li[2]/span[2]")
#     input_content('class name', 'nui-editableAddr-ipt', '764904579@qq.com')
#     input_content_list('class name', 'nui-ipt-input,2', '测试邮件')
#     time.sleep(5)
#     switch_frame('class name', 'APP-editor-iframe')
#     input_content("class name", 'nui-scroll', '你的梦想是什么？')
#     switch_frame_out()
#     click('xpath', '/html/body/div[2]/div[1]/div[2]/header/div/div[1]/div/span[2]')
#     close_browser('')
