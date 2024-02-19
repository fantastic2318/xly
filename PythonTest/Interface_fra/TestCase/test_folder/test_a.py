import pytest

#@pytest.mark.run(order=2)
def test_a_1():
    print('test_a_1')

@pytest.mark.last # 最后一个执行
#@pytest.mark.run(order=1)
def test_a_2():
    print('test_a_2')


@pytest.mark.second_to_last  # 倒数第二个执行
def test_b_1():
    print('test_b_1')


@pytest.mark.run('first')
def test_b_2():
    print('test_b_2')

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
pytest-ordering 修改 执行顺序 @pytest.mark.run(order=2)
@pytest.mark.second 效果同上 

 pytest -vs test_a.py --html=aa.html   生成测试报告名字
"""