import pytest

@pytest.mark.run(order=4)
def test_1_1():
    print('test_1_1')


@pytest.mark.run(order=3)
def test_1_2():
    print('test_1_2')



# @pytest.mark.second
# def test_1_1():
#     print('test_1_1')
#
#
# @pytest.mark.first
# def test_1_2():
#     print('test_1_2')
"""
同一个文件夹下  测试用例文件 按照ASCII码顺序执行的
一个文件内部，测试用例方法 按照自上而下顺序执行
pytest-ordering 修改 执行顺序 @pytest.mark.run(order=2)  可以修改多文件之间的测试用例方法的执行顺序
@pytest.mark.second 效果同上
"""