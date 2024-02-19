import time
from selenium import webdriver
path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(executable_path=path)

#driver.get('http://www.baidu.com')
# 通过id 查找控件
#obj = driver.find_element(by='id', value='kw').send_keys('wahaha')

# 通过name 查找
#driver.find_element(by='name',value='wd').send_keys("娃哈哈")
#time.sleep(5)
#print(type(obj))
"""
v1.0 js类库 通过浏览器内置的翻译器 翻译执行代码  浏览器安全限制
v2.0 js类库+webdriver 直接去调用浏览器和系统的方法 绕过浏览器的安全限制 封装了
v3.0  优化 
"""
# class html 样式类
# 通过classname 查找
#driver.find_element('class name', 'hot-refresh-text').click()
#time.sleep(3)

# 通过link_text partial_link_text 查找
#driver.find_element('link text', '新闻').click()
#time.sleep(3)
# 超链接文本太长时 使用部分超链接文本查找
#driver.find_element('partial link text', 'hao12').click()
#time.sleep(3)
# 通过xpath css 查找 （层级关系 需要自己看）
#driver.find_element('xpath','//*[@id="kw"]').send_keys('hahah')
#time.sleep(3)
#driver.find_element('css selector','#kw').send_keys('jjjj')
#time.sleep(3)


# 网址类 get()
#driver.get('http://www.baidu.com')
# 刷新
#driver.refresh()
# 后退
#driver.back()
# 前进
#driver.forward()

# 获取当前网站的网址
url = driver.current_url
# title 获取标题
t = driver.title
# page_source()
s = driver.page_source
# 窗口类
# 最大化
# span 标签 可以使用link text
#driver.maximize_window()
#time.sleep(5)
#print(f'点击百度百科之前 现在窗口是{c} 所有窗口是{d}')
# driver.find_element('id', 'kw').send_keys('米兰')
# driver.find_element('id', 'su').click()
# time.sleep(5)
# 返回当前窗口的句柄（标识符）
#driver.find_element('partial link text', '百度百科').click()
#c = driver.current_window_handle
# 返回所有窗口句柄
#d = driver.window_handles
#print(f'点击百度百科之前 现在窗口是{c} 所有窗口是{d}')
# 切换窗口句柄
#driver.switch_to.window(d[-1])
#driver.find_element('link text', '首页').click()
#driver.switch_to.window(c)

# 鼠标
from selenium.webdriver.common.action_chains import  ActionChains
# 鼠标悬浮控件
#ActionChains(driver).move_to_element(driver.find_element('id','s-usersetting-top')).perform()
#driver.find_element('link text','设置').click()

driver.get('http://mail.163.com')
time.sleep(3)
# 根据tag name(input  span iframe )查找
tmp_iframe = driver.find_element('tag name', 'iframe')
# 切换到iframe中
driver.switch_to.frame(tmp_iframe)
time.sleep(2)
driver.find_element('name','email').send_keys('fantastic2318')
driver.find_element('name','password').send_keys('fantastic12306')
driver.find_element('id', 'dologin').click()
time.sleep(5)
# 写信
driver.refresh()
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

driver.find_element('xpath', '/html/body/div[1]/nav/div[1]/ul/li[2]/span[2]').click()
time.sleep(3)
driver.find_element('class name', 'nui-editableAddr-ipt').send_keys('764904579@qq.com')
# driver.find_element('class name', 'nui-ipt-input').send_keys('测试')
driver.find_elements('class name', 'nui-ipt-input')[2].send_keys('你吃饭了没')
driver.switch_to.frame(driver.find_element('class name', 'APP-editor-iframe'))
driver.find_element('class name', 'nui-scroll').send_keys('你吃饭了么')
driver.switch_to.default_content()
driver.find_element('xpath', '/html/body/div[2]/div[1]/div[2]/header/div/div[1]/div/span[2]').click()






# 切换回原iframe
# driver.switch_to.default_content()
# driver.find_element('link text','手机APP下载').click()




# 双击/单击 自己学习
"""
一般情况下 一个网页只有一对<html></html>
但是 <iframe>中可以内嵌HTML
<body>
   <iframe>
      <html>
      
      </html>
   </iframe>
</body>
"""

# 文本输入
# send_keys()
# click()
# clear() 清空
# 控件是否显示 is_displayed()
# 控件是否可用 is_enabled()
# 获取元素的属性 get_attribute()
# driver.find_element('id', 'kw').send_keys('whhahaha')
# driver.find_element('id','kw').clear()
# print(driver.find_element('id','kw').is_displayed())
# print(driver.find_element('id','kw').is_enabled())
# print(driver.find_element('id','kw').get_attribute('id'))
# time.sleep(3)


