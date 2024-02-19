# -*- coding: utf-8 -*- 
# @Time : 2023-12-10 09:41 
# @Author : kunp
# @File : 1210.py 
# @Software: PyCharm


# homework
'''
[4,1,6,9,10,2,5]

选择排序
def select_sort(lst):
    for i in range(len(lst)-1):
        min = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]  # => lst[0],lst[1] = lst[1],lst[0]
    print(lst)

select_sort([4,1,6,9,10,2,5])


列表中第二大的值
[4,1,6,9,10,2,5]

def find_seceond(lst):
    max_value = sec_max_value = 0
    for i in lst:
        if i >= max_value:
            sec_max_value = max_value
            max_value = i
        elif i >= sec_max_value and i < max_value:
            sec_max_value = i

    print(f'第二大的值是{sec_max_value}')

find_seceond([4,1,6,9,10,2,5])
'''


# selenium
import time

from selenium import webdriver

from data_fra.Util.find_element import locate_element

'''
selenium 1.0  （js 类库)  + webdriver ---> selenium2.0 --->(优化) selenium 3.0 
'''
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://www.baidu.com/")

# 通过id 查找控件
# driver.find_element("id", "kw").send_keys('娃哈哈')

# 通过name 查找
# driver.find_element('name', "wd").send_keys('娃哈哈')


# 通过class name 查找
# time.sleep(3)
#
# driver.find_element('class name', "hot-refresh-text").click()

# 通过 link_text  partial_link_text  查找
# driver.find_element('link text', 'hao12').click()

# driver.find_element('partial link text', 'hao12').click()

# 通过  xpath css 查找
# time.sleep(30)

# driver.find_element('xpath', '//*[@id="kw"]').send_keys('娃哈哈')

# driver.find_element('css selector', '#kw').send_keys('娃哈哈')

# 网址类
# 访问网站 get driver.get("http://www.baidu.com/")
# refresh() 刷新
# driver.refresh()

# 前进  后退

# time.sleep(2)
#
# driver.get("http://www.sina.com.cn")
#
# time.sleep(2)

# 后退
# driver.back()
#
# time.sleep(2)

# 前进
# driver.forward()
#
# time.sleep(2)

# current_url  获取现在访问的网址
# title  页面title
# page_source  获取页面源代码
# print(f'当前访问网址是{driver.current_url}')
# print(f'当前访问网址title是{driver.title}')
# print(driver.page_source)

# 窗口类
# 最大化
# driver.maximize_window()
# driver.find_element('id', 'kw').send_keys('米兰')
# driver.find_element('id', 'su').click()
# time.sleep(3)
# # 当前窗口句柄
# now_window = driver.current_window_handle
# # 所有窗口句柄
# all_widnows = driver.window_handles
# print(f'点击百度百科之前，现在的窗口是 {now_window}, 所有窗口是{all_widnows}')
# driver.find_element('partial link text', '百度百科').click()
# now_window = driver.current_window_handle
# all_widnows = driver.window_handles
# print(f'点击百度百科之后，现在的窗口是 {now_window}, 所有窗口是{all_widnows}')
# # 切换窗口句柄
# driver.switch_to.window(all_widnows[-1])
# driver.find_element('link text', '首页').click()
#
# driver.switch_to.window(now_window)
# driver.find_element('link text', '百度首页').click()

# 元素类
# 文本输入  send_keys()
# 清空 clear()
# click()
# 控件是否显示 is_display()
# 控件是否可用 is_enabled()
# 获取元素的属性  get_attribute('name')
# driver.find_element('id', 'kw').send_keys('wahaha')
# driver.find_element('id', 'kw').clear()
# print(driver.find_element('id', 'kw').is_enabled())
# print(driver.find_element('id', 'kw').is_displayed())
# print(driver.find_element('id', 'kw').get_attribute('id'))


# 鼠标悬停
# from selenium.webdriver.common.action_chains import  ActionChains
# # 鼠标悬浮到某个控件上
# ActionChains(driver).move_to_element(driver.find_element('id', 's-usersetting-top')).perform()
#
# driver.find_element('link text', '搜索设置').click()


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://mail.163.com/")
time.sleep(2)
# tmp_frame = driver.find_element('tag name', 'iframe')
tmp_frame = locate_element(driver, 'tag name', 'iframe')
# 切换frame
driver.switch_to.frame(tmp_frame)
locate_element(driver, 'name', 'email').send_keys('zhangming002')
locate_element(driver, 'name', 'password').send_keys('zmkmzmkm')
locate_element(driver, 'id', 'dologin').click()
time.sleep(3)
# # 写信
# driver.find_element('xpath', '/html/body/div[1]/nav/div[1]/ul/li[2]/span[2]').click()
# time.sleep(2)
# # 收件人
# driver.find_element('class name', 'nui-editableAddr-ipt').send_keys('1552599101@qq.com')
# # 主题
# driver.find_elements('class name', 'nui-ipt-input')[2].send_keys('你吃饭了没')
# # 切换 frmae， 输入 正文
# driver.switch_to.frame(driver.find_element('class name', 'APP-editor-iframe'))
# driver.find_element('class name', 'nui-scroll').send_keys('你的梦想是什么？')
# # 发送
# driver.switch_to.default_content()
# driver.find_element('xpath', '/html/body/div[2]/div[1]/div[2]/header/div/div[1]/div/span[2]').click()
#
#
time.sleep(5)




