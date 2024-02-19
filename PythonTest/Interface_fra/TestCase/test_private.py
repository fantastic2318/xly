import pytest
'''
仅在一个文件中定义的fixture，只能这个文件中的函数、类引用，其他文件中的函数类都不能引用
'''

@pytest.fixture()
def func_private():
    print('这是私有的前置')
    yield
    print('这是私有的后置')


def test_f1(func_private):
    print('f1')