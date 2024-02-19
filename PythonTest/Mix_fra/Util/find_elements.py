from pprint import pprint

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def locate_element(driver, find_type, expression):
    """
    查找控件元素
    :param driver: driver
    :param find_type:
    :param expression:
    :return:
    """
    # 默认每隔0.5s查询,每隔2秒内查询
    try:
        element = WebDriverWait(driver, 10).until(lambda driver:driver.find_element(by=find_type, value=expression))
        return element
    except Exception as e:
        raise e


def locate_elements(driver, find_type, expression):
    """
    查找多个控件
    :param driver: driver
    :param find_type:
    :param expression:
    :return:
    """
    # 默认每隔0.5s查询,每隔2秒内查询
    try:
        #pprint(f'{find_type}---元素列表---{driver.find_elements(by=find_type, value=expression)}')
        element = WebDriverWait(driver, 10).until(lambda driver:driver.find_elements(by=find_type, value=expression))
        return element
    except Exception as e:
        raise e


