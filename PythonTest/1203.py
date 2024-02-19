#  实例变量和类变量 同名 优先取类变量  不推荐写法 类变量使用对象名调用
#
# 迭代器 生成器
# 调用字符串的内置的iter()
# 返回了一个定义__next__() 迭代器对象
# __next__()逐一访问'abc'中的元素
# 当元素用尽时 将引发StopIteration 异常 通知终止for循环
for s in 'abc':
    print(s)

o = iter('abc')  # o是字符串迭代器对象
print(type(o), o)  # 字符串对象类型
print(dir(o))  # 对象拥有的方法

# 通过next()方法 来调用o.__next__()
# print(next(o))
# print(next(o))
# print(next(o))
print(o.__next__())
print(o.__next__())
print(o.__next__())
#print(o.__next__())
# 同样适用于 列表迭代器 元素迭代器对象

# 可迭代对象
# 对象在内部实现了一个 __iter__()方法 那么这个对象就是可迭代对象
# 迭代器同时实现了__iter__(),__next__()方法 他就是一个迭代器
# 一个迭代器对象一定是一个可迭代对象，反之 不正确
from collections.abc import Iterable, Iterator
class Color:

    def __init__(self):
        self.color = ['red','black','yellow','blue','white']

    def __iter__(self):
        pass

color = Color()
# 判断对象是否为 可迭代对象 Iterable
print(isinstance(color, Iterable))
# 判断对象是否为 迭代器对象
print(isinstance(color, Iterator))


class Iter_demo:

    def __init__(self,data):
        self.data = data
        # self.index = len(data)
        self.index = -1

    # 声明 是一个可迭代对象
    def __iter__(self):
        return self
    # next() 调用__next__() 创建一个迭代器
    def __next__(self):
        # if self.index == 0:
        if self.index == len(self.data)-1:
            raise StopIteration
        # self.index -= 1
        self.index += 1
        return self.data[self.index]


a = Iter_demo('abc')
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
print(a.data)
for i in a:
    print(i)

# 生成器
"""
列表递推式 [i*3 for i in range(100)]
"""

# 生成器函数 yield 关键字 返回一个值后 还能从退出的地方继续运行下去 且自动实现了迭代协议（返回一个迭代器）
# 生成器本身是一个迭代器对象
def gen_func():
    print("yield 1......")
    yield 1

    print('yield 2...')
    yield 2

# g  = gen_func()
# print(g)
# print(isinstance(g,Iterator))
# for i in g:
#     print(i)

def gen_func(num):
    for x in range(num):
        print(f'yield{x}')
        yield x*2
        print(f'yieldjajajaj')
g = gen_func(5)
next(g)
next(g)
next(g)

# 在大数据的情况 加载一行处理一行 使用生成器
# 生成器表达式
l = [i*3 for i in range(100)] # 速度快
g = (i*3 for i in range(100)) # 省空间