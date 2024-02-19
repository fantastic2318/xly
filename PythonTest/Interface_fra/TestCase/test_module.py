"""
1.使用module级别的fixture，要把fixture传入到整个文件运行的第一个函数的参数，文件即module，
2.module级别的fixture放到类外面的函数中，否则效果跟类级别的一致
3.fixture可以叠加到
"""


def test_05(func_m):
    print('test_05')


def test_06():
    print('test_06')


class TestClass():

    def test_01(self, func_m):
        print('TestClass_test_01')

    def test_02(self):
        print('TestClass_test_02')

    def test_03(self):
        print('TestClass_test_03')