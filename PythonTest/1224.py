import logging
from loguru import logger

logger.debug("debug")
logger.info("debug")
logger.warning("debug")
logger.error("debug")
logger.success("debug")
logger.critical("debug")
# 创建一个log文件、每天零点会创建一个新的日志文件
#logger.add("log.log", rotation='00:00')
# 超过500M创建一个新文件
#logger.add("log.log", rotation='500M')
# 每隔一周创建一个新文件
#logger.add("log.log", rotation='1 week')
# 日志保留15天
#logger.add("log.log", retention='15 Days')


"""
test case :基类 TestCase 用例方法以Test开头 执行顺序 按照方法名的ASCII码值去排序
2.Test fixture ：测试夹具 测试固件 测试用例环境的搭建和销毁（前置条件SetUp和后置条件TearDown）
3、test suite 测试套件 把需要一起执行的测试用例集中一块执行 可以使用TestLoader 来加载测试用例放到测试结果
4、test runner 执行测试用例 返回测试结果

assertEqual(a,b,msg=None)  a==b
assertNotEqual(a,b,msg=None)  a==b
assertTure(x,msg=None)  x is True
assertFalse(x，msg=None) x is False
assertIs(a,b，msg=None) a is b
assertIsNot(a,b，msg=None) a is not b
assertIn(a,b，msg=None)  a in b
assertIsNone(a,b，msg=None)  a is None
assertIsInstance(a,b，msg=None) isInstance(a,b)

AssertinError 不通过
"""


"""
测试步骤 test steps

    --test object测试对象 {location_type, location_express}

    --test action 对象执行的动作 {相应的方法名,代码中有相应的方法}
    
    --test data 测试数据
    
    读取Excel中的步骤
    Excel: 总组织sheet  每个场景单独一个的sheet  

"""
"""
关键字驱动+unittest/pytest
根据excelindex 拼接成测试报告
"""