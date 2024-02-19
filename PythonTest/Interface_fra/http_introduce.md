## http 构成
1、request-line
请求方法
要访问的资源（URL）
HTTP 版本（协议版本号 状态码 状态消息）
2、headers
用来说明 服务器要使用的一些附加信息
空行（headers和request-bodys有空行）
3、request-body
Accept:客户端可接收的类型

## 响应码
常见场景举例
5XX  服务器错误 
500  Internal server Error 服务器遇到意料不到的错误 不能完成客户端的请求
501  Not Implemented  服务器不支持实现   服务端接口是get请求，客户端请求该接口时使用post
502  Bad gateway 网关错误
503  server Unbelievable 
504  gateway timeout 

4XX  客户端错误 请求地址写错了 请求包含语法错误 或者请求无法实现
400 Bad Request 请求出现语法错误
401 Unauthorized 访问请求未经授权
403 Forbidden 资源不可用
404 Not Found 无法找到资源所在位置，URL拼写是否有误
3XX  重定向错误  为了完成请求 必须进一步的执行动作
2XX 200
1XX 信息 请求收到会继续处理


url 连接后都发生什么
1. 域名DNS解析-> ip地址
2.TCP三次握手 -> 服务器建立链接
3.发起HTTP请求
4.服务器响应HTTP请求，返回响应报文
5.浏览器 接受响应报文，进行页面渲染，展示
6.断开TCP链接，四次挥手

## pytest
1、灵活简单 容易上手 支持参数化
2、简单的功能测试、复杂的功能测试
3、自定义扩展、多CPU分发

## pytest 记录
1.l测试用例类中的方法以test*开头
2.测试用例的类名必须以Test*开头
3.类中不能有__init__方法
4.文件名以test_开头 或者 _test结尾文件 会被识别为测试文件
5.自定义以上的识别规则 在项目根目录下新建pytest.ini文件

#### pytest终端运行
运行参数介绍
-v 用于显示 每个测试函数的执行结果
-q 只显示 整体测试结果
-s 显示测试函数中的print()输出
-x 允许失败的次数 --exitfirst 第一次失败就退出 --maxfail=2 允许测试用例失败几次
-m 执行标记的测试用例
-k 根据表达式运行指定的测试用例

文件中运行
pytest为收集到的测试用例分配一个唯一的标记nodeid 是由 模块名::说明符(可以是类型 函数名 parametrize标记赋予的参数) 组成
-- ignore=文件名 忽略某一个测试文件  测试函数(使用nodeid)  测试文件夹(测试路径)  pytest -s --ignore=test_ficture_value.py

异常
assert a=b, 'z这是常识错误'

#### fixture
作用：测试用例环境准备、清理等
1.公有的fixture、必须定义在测试用例文件夹同级目录下
2.一个普通函数使用@pytest.fixture装饰就是fixture
3.fixture的前置和后置是放在一起的，一个函数内的
4.使用yield区分前置和后置
5.fixture中不一定有yield，可以只有前置操作 没有后置操作,也可以没有前置只有后置






