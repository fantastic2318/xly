import pytest


def fun(x):
    return x+1


def myfunc():
    raise ValueError('123 raised')
    

# 使用上下文捕捉器，如果捕捉到异常 说明预计此处有异常，测试用例执行成功
def test_match():
    with pytest.raises(ValueError):
       myfunc()


def test_a():
    print('这是测试a')
    assert fun(5) == 6


def test_b():
    print('这是测试b')
    assert fun(1) == 3, '这是常识错误'


if __name__ == '__main__':
    pytest.main(['-v', 'test_demo.py::test_a'])
