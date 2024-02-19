import pytest
'''
fixture 参数化
'''

@pytest.fixture(params=['11', '22'])
def my_method(request):
    return request.param


def test_use_fixture(my_method):
    print(my_method)