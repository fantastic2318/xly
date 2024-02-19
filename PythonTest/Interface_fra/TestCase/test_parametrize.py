import pytest

'''
def parametrize(argnames,argvalues,indirect=False,ids=None,scope=None):

1.argnames  指定的参数名 可以是用逗号隔开的字符串,也可以是一个元组/列表、集合
* 定义了，就要用到
* 被修饰的函数中不能有默认值
* 会覆盖掉同名的fixture
* 被修饰的函数必须有同名的参数，跟argnames一致
2.argvalues 指定参数的值 可迭代对象 对应argnames参数的值
* argvalues 返回的迭代元素长度 必须和 argnames声明的参数个数相等,可以是列表 元组 集合（因为去重不推荐使用）
3.indirect=True  pytest会吧argname 当做函数执行 并且将argvalues作为参数传入到argnames函数中
test_getuser[1-2-3-4-5]非常复杂 所以使用ids标记
4.ids给每一组参数自定义名字，运行结果以ids标记
'''
#会覆盖住同名的fixture
# @pytest.fixture()
# def excepted():
#     return 1


# @pytest.mark.parametrize('input,excepted', [(1, 2), (3, 4)], ids=['one', 'two'])
# #@pytest.mark.parametrize(['input,excepted'], [(1, 2), (3, 4)])
# def test_sample(input, excepted):
#     assert input + 1 == excepted


@pytest.mark.parametrize('input', [1, 2, 3])
@pytest.mark.parametrize('testoutput, excepted', [['a', 'b'], ['c', 'd']])
def test_sample(input, testoutput, excepted):
    print(input, testoutput, excepted)


# 被修饰的函数的参数不能有默认值
# @pytest.mark.parametrize('input,excepted', [(1, 2), (3, 4)])
# def test_sample1(input, excepted=0):
#     assert input + 1 == excepted


#被修饰的函数必须有同名的参数
# @pytest.mark.parametrize('input,excepted', [(1, 2), (3, 4)])
# def test_sample(a, b):
#     assert a + 1 == b

# 单个参数
# @pytest.fixture()
# def getuser(request):
#     user = request.param
#     print(f'获取用户：{user}')
#     return user
#
# data = ['kunp','cc','laoz']
#
# @pytest.mark.parametrize('getuser',data, indirect=True)
# def test_getuser(getuser):
#     print(f'输出用户信息{getuser}')

# 多个参数
# data1 = [{'username':'kunp','password':'123456'}, {'username':'kunp1','password':'234567'}]
#
#
# @pytest.fixture()
# def getuser(request):
#     param = request.param
#     print(f'获取用户名:{param["username"]}, 获取密码为:{param["password"]}')
#     return param
#
#
# @pytest.mark.parametrize('getuser', data1, indirect=True)
# def test_getuser(getuser):
#     print(f'获取用户名:{getuser["username"]}, 获取密码为:{getuser["password"]}')