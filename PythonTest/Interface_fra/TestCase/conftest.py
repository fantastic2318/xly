'''
公有的fixture 写于此 conftest.py文件名固定
fixture函数参数定义四种作用级别
函数级别 scope='function' 默认
类级别 scope='class'
模块级别 scope='module'
会话级别 scope='session'

@pytest.fixture(scope='function', autouse=True) 会自动引入该级别fixture
会优先执行自动引入的fixture，然后再执行手动引入的
'''
import pytest


@pytest.fixture(scope='function')
def func():
    print('这是函数前置操作')
    yield
    print('这是函数后置操作')


@pytest.fixture(scope='function')
def func_1():
    print('这是函数前置操作1')
    yield
    print('这是函数后置操作1')


# @pytest.fixture(scope='function', autouse=True)
# def func_auto():
#     #print('\n这是自动加的函数前置操作')
#     yield
#     print('\n这是自动加的函数后置操作')

@pytest.fixture(scope='class')
def func_c():
    print('\n这是类前置操作')
    yield
    print('\n这是类后置操作')


@pytest.fixture(scope='module')
def func_m():
    print('\n这是模块前置操作')
    yield
    print('\n这是模块后置操作')



