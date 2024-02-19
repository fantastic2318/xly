"""
1.setup中执行报错后，teardown不会执行
2.模块级别的前置和后置
"""
import pytest


# def setup_module(module):
#     print('这是模块级别的前置')
#
#
# def teardown_module(module):
#     print('这是模块级别的后置')

# 只对类外面的函数生效
def setup_function():
    print("这是函数级别的前置")

def teardown_function():
    print("这是函数级别的后置")

def test_1():
    print("TestClass_test1")

'''
类级别的前置和后置
1.setup中执行报错后，teardown不会执行 同样适用于类级别
'''


class TestClass:
    def setup_method(self):
        # print(1/0)
        print('这是类中方法级别的前置')

    def teardown_method(self):
        print('这是类中方法级别的后置')

    @classmethod
    def setup_class(cls):
        # print(1/0)
        print('这是类级别的前置')

    @classmethod
    def teardown_class(cls):
        print('这是类级别的后置')


    def test_2(self):
        print("TestClass_test2")

    def test_3(self):
        print("TestClass_test3")

"""
1.一个普通函数使用@pytest.fixture装饰就是fixture
2.fixture的前置和后置是放在一起的，一个函数内的
3.使用yield区分前置和后置
"""
@pytest.fixture
def func1():
    # 前置操作
    yield
    # 后置操作