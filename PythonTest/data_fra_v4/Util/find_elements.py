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



