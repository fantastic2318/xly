"""
函数名 作为测试用例函数传递一个参数,实际
1.使用class级别的fixture，只要把fixture传入类中其中一个函数即可，无论几个函数 ，只要有一个函数传入就会生效
2.类外面的函数中传入类级别的fixture，作用效果同函数级别的fixture

"""


def test_05(func_c):
    print('test_05')


def test_06(func_c):
    print('test_06')


class TestClass():

    def test_01(self, func_c):
        print('TestClass_test_01')

    def test_02(self):
        print('TestClass_test_02')

    def test_03(self, func_c):
        print('TestClass_test_03')