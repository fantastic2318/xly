"""
Java 以项目/工程为单位
每一个项目都是独立环境

Python 所有项目都公用同一套环境

"""
"""

PO模式(page object) + 三层架构
一个页面看成一个对象
对元素的操作 看成 API
对象层 Objects：用于存放页面对象（包含了哪些控件操作、元素定位）
逻辑层 Module:用于存放一些 封装好的功能 登录 登出
业务层/脚本层Scripts:真正的测试用例



"""

"""
XXXX.ini
节 键-值（参数）
[节1]
key1=value1
key2=value2
节2前所有参数都属于节1
[节2]
key1=value1
key2=value2
"""
"""
data_fra_v1 :初步实现PO模式
data_fra_v2: 将页面元素定位type,定位expression参数化
data_fra_v3: 将登陆的账号 密码参数化 数据驱动
"""