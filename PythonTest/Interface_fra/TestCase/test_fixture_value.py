import pytest
"""
函数名 作为测试用例函数的一个参数，实际代表的是fixture的返回值，并不是函数本身
"""

@pytest.fixture
def func():
    obj = {'a': 1, 'b': 2}
    return obj


def test_01(func):
    print('\ntest_01')
    for key, value in func.items():
        print(key, value)


def test_02(func):
    print('\ntest_02')
    for key, value in func.items():
        print(key, value)