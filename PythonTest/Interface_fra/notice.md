## 同视频不符之处
1.pytest -vs test_parametrize.py::test_sample[1-2]  该方式执行不成功
2.@pytest.mark.parametrize(['input,excepted'], [(1, 2), (3, 4)])  执行报错
3.    def setup_method(self):
        # print(1/0)
        print('这是类中方法级别的前置')

    def teardown_method(self):
        print('这是类中方法级别的后置')
该方法中 不能只使用setup teardown 也会报错
不知道以上不是跟pytest版本有关