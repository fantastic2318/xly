"""
global可以在任何地方修饰变量，而且被global修饰的变量直接被标识为全局变量，
对该变量修改会影响全局变量的值，但不影响函数中未被global修饰的同名变量（依然是局部变量），
nonlocal只能在嵌套函数（可能还有其他的地方，我还没有检查）中使用，
用于标识嵌套函数中的变量是包含该嵌套函数的函数中的同名变量，在嵌套函数中修改变量会影响函数中的变量。
如果在函数中使用global修饰了变量，那么在嵌套函数中用nonlocal修饰同名变量会发生报错，因为nonlocal表示该变量在函数中已经定义，
但检查时因为同名变量被global修饰为全局变量，所以不存在同名的局部变量，从而导致错误
"""

# 调用外层函数时 运行到def内部时，仅仅是完成对函数的定义 而不会去调用内层函数
# 函数内部的作用域 在函数调用结束后 会被清除掉 enclosing作用域 在嵌套函数返回之后仍然有效

t = lambda x:'big' if x>5 else 'small'
lambda : print('无参数打印')
print(lambda : print('无参数打印'))

foo = [1,2,5,29]
foo1 = [x*3+5 for x in foo]
foo2 = list(map(lambda x: x*3+5, foo))

list1 = [1,2,3,4]
list2 = [2,3,4,5]
list3 = list(map(lambda x,y: x+y,list1,list2))
print(list3)


fooo = [2,18,9,22,17,8,2]
foo3 = list(filter(lambda x: x%3==0 ,fooo))

#f = [1,2,3,4]  x*10+y
# reduce(f,iter)  返回一个值 不是迭代器对象
f = [1,2,3,4]
from functools import reduce
ff = reduce(lambda x, y: x*10+y, f)
print(ff)


class Car:
    def __init__(self,brand,age):
        self.brand = brand
        self.age = age

    def broke(self):
        print('刹车')

    def add(self):
        print('在加速')


class Mini_Car(Car):
    def __init__(self, brand, age,weight):
        super(Mini_Car, self).__init__(brand, age)
        self.weight = weight
    def print_weight(self,weight):
        print(f"打印{weight}")
    def broke(self):
        print("打印不同")


mini = Mini_Car("吉利", 10, 10000)
mini.broke()

import abc
class Car1(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def speed1(self):
        pass
