import sys

import pytest


# @pytest.mark.skipif(True, reason="just skip....")
# def test_1():
#     print('test1')
#
#
# @pytest.mark.skip(reason="just skip too...")
# def test_2():
#     print('test2')
#
#
# @pytest.mark.xfail
# def test_3():
#     assert 1 == 1 # Xpass 预期失败 但是成功的用例
#     assert 1 == 2  # XFAIL 预期失败 结果失败的用例


# @pytest.mark.xfail(sys.version_info < (3, 10), reason="只有当条件表达式成立 标记才使用")
# def test_3():
#     assert 1 == 1 # Xpass 预期失败 但是成功的用例
#     assert 1 == 2  # XFAIL 预期失败 结果失败的用例


# def test_4():
#     print('11')
#     pytest.xfail('接口请求失败、预期错误 ')


@pytest.mark.parametrize(
    ['n', 'expected'],
    [
        (2, 1),
        pytest.param(2, 3, marks=pytest.mark.xfail(), id="XFAIL"),
        pytest.param(1, 2, marks=pytest.mark.skip(reason='无效参数'), id='SKIP'),
        pytest.param(1, 2, marks=pytest.mark.skipif(sys.version_info < (3, 10), reason='need skip'), id='SKIPIF')
    ]
)
def test_param(n, expected):
    assert 2/n == expected