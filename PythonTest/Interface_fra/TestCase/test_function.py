'''
1.叠加传入fixture，装饰顺序为先传入的fixture先先装饰
2.引用fixture还可以使用@pytest.mark.usefixtures('func')
'''
import pytest


def test_a(func, func_1):
    print('test_a')


@pytest.mark.usefixtures('func_1')
@pytest.mark.usefixtures('func')
def test_b():
    print('test_b')


@pytest.mark.usefixtures('func', 'func_1')
def test_c():
    print('test_c')

'''
b不可以使用func_private 原因是在普通文件module中定义的fixture，只能该文件中的函数或者类使用，
其他文件不可以使用
'''
# def test_d(func_private):
#     print('test_d')
