# 函数式编程
# 统计字符串中字符出现的次数 使用列表生成式(字典也可以使用)
a = 'adfdfsfadf'
dict1 = {i:a.count(i) for i in set(a)}
print(dict1)

# map(func,iter1,iter2,....)   将序列中的每一个元素都作用于func func可有多个参数
a = [6, 1, 3]
b = [5, 2, 7]
print(list(map(lambda x, y: x+y, a, b)))

str2 = ['xxx', 'yyy']
iteralll = map(lambda x: x.upper(), str2)
# 得到一个迭代器对象 需要使用list()变成列表
print(list(iteralll))

#f = [1,2,3,4]  x*10+y
# reduce(f,iter)  返回一个值 不是迭代器对象
f = [1,2,3,4]
from functools import reduce
ff = reduce(lambda x, y: x*10+y, f)
print(ff)

# 找出闰年年份
ll = [2002,2004,1999,2000,1986,1992]
# filter(func,iter1) 返回一个遍历序列中、满足指定条件的迭代器 func只有一个参数
print(list(filter(lambda x: True if x % 4 == 0 or x % 400 == 0 else False, ll)))

from functools import reduce
# enumerate(iter,startIndex) startIndex 开始计算的下标和元素 返回的是迭代器对象
# 打印对应字符集齐序号
list1 = ['a','b','c','d']
print(list(enumerate(list1,1)))

# 按照分数大小排序
score = [('c',100),('xiao',90),('ni',91)]
#sorted(liter1,key,reverse)
b = sorted(score, key=lambda x: x[1],reverse=True)
print(b)
score.sort(key=lambda x:x[1],reverse=True)
print(score)
# 按照第一个参数的长度排序
c = sorted(score, key=lambda x: len(x[0]))
print(c)

# 返回 {'name':'kp','sex':'M','age':20}
ll = ['name', 'sex', 'age']
ll1 = ['kp', 'M', 20]
# d = reduce(lambda x, y: {x: y}, ll, ll1)
# zip(iterA,iterB,....) 从每个可迭代的对象选取元素组成:元组返回
d = dict(zip(ll, ll1))
print(d)

print(any([0, 0, 1])) # 列表中只要有一个为True 就返回True
print(all([1, 1, 1]))

# 面向对象编程 类 实例  减少代码冗余
"""
类：模板
实例：根据模板创建出来的一个对象
属性： 这类东西具有的属性
方法：这类东西可以做的事情
"""
# class Triangle(object):
class Triangle:
    # 初始函数、创建对象时默认调用
    # self 构建的实例的本身
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def get_s(self):
        return self.a * self.b / 2

    def get_c(self):
        return self.a+self.b+self.c


t1 = Triangle(1,1,2)
print(t1.get_c())
t2 = Triangle(2,4,3)
print(t2.get_c())

# 面向对象特性：继承 封装 多态
# 继承


class Mini_Triangle(Triangle):
    def __init__(self,a,b,c,d):
        #Triangle.__init__(self,a,b,c)
        # 使用父类的初始化函数
        super(Mini_Triangle, self).__init__(a, b, c)
        self.d = d

    def get_d(self):
       return '新方法'
    # 重写父类的方法
    def get_c(self):
        return self.a+self.b+self.c+self.d

mini_t = Mini_Triangle(1,2,3,4)
print(mini_t.a)
print(mini_t.get_c()) # 继承了父类的方法

# 新式类 经典类
# 由内置类派生出来的为经典类  否则为新式类 广度优先的方式去查找继承类
class P1:
    def foo(self):
        print("p1-foo")

class P2:
    def foo(self):
        print("p1-foo")
    def bar(self):
        print('p2-bar')

class C1(P1,P2):
    pass

class C2(P1,P2):
    def bar(self):
        print('c2-bar')

class D(C1,C2):
    pass

d = D()
d.bar()
d.foo()

# 多态 多态性
# 多态 一类事物的多种形态

# 抽象类 不能实例化的类

import abc
# 继承抽象类
class TransTools(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    # 抽象方法
    def say_speed(self):
        pass

# 多态性 （一个接口 多个实现） 具有不同功能的函数  可以使用相同的函数名， 依赖继承 抽象类
# 这样 就可以用一个函数名调用不同内容的函数
"""
向不同的对象发送同一条消息 不同的对象在接受时产生不同的行为 每个对象可以用自己的凡是去响应共同的消息
不同功能使用相同的函数名
"""
class Car(TransTools):
    def say_speed(self):
        print("i am a Car,100km/h")


class Ship(TransTools):
    def say_speed(self):
        print("i am a Ship,10km/h")


class Fly(TransTools):
    def say_speed(self):
        print("i am a Car,1000km/h")

c = Car()
s = Ship()
f = Fly()

def mul_demo(obj):
    obj.say_speed()

mul_demo(c)
mul_demo(s)

# 类变量和实例变量
"""
类变量 用于类  所有实例共享的属性 定义在类里面 实例方法外的变量 属于所有实例共享的  类直接调用 实例直接调用
实例变量  用于每一个实例特有的数据  定义在实例方法里面 
"""
class Dog:
    kind = []
    kind1 = 'animal'
    name = '珍珠'
    def __init__(self,name):
        self.name = name


d1 = Dog("小白")
d2 = Dog("小黑")
d1.kind.append('animal')
d2.kind1 = "paxing"
print(d2.kind) # 当类变量是可变对象时、一个实例调用改变 整体调用都会改变
print(Dog.kind)
print(d1.kind1) # 当类变量为不可变量对象时、一个实例调用改变、整体调用都不会改变
print(d1.name) # 类变量和实例变量同名时、优先选择实例变量


