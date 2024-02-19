# 冒泡排序优化
#常规写法
def bubbleSort_v1(list1):
    for i in range(len(list1) - 1, -1, -1):  # 行数
        for j in range(0, i):  # 每一行交换的次数
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
        print(f"第{i}轮排序后 表现为{list1}")
    return list1

# 轮数优化
print(bubbleSort_v1([2, 3, 1, 9, 12,43,45]))



#标记是否有过交换 针对交换轮数
def bubbleSort_v2(list1):
    for i in range(len(list1) - 1, -1, -1):  # 行数
        is_sorted = False
        for j in range(0, i):  # 每一行交换的次数
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
                is_sorted = True
        print(f"第{i}轮排序后 表现为{list1}")
        if  is_sorted == False:
            break
    return list1
print(bubbleSort_v2([2, 3, 1, 9, 12,43,45]))

#标记交换位置、针对每轮排序的两两交换次数进行优化--》对序列区的界定-->每一轮排序后、记住最后一次元素交换的位置
def bubbleSort_v3(list1):
    # 最后一次交换的位置
    last_exchange_index = 0
    # 无序区的边界
    sort_border = len(list1) - 1
    for i in range(len(list1) - 1, -1, -1):  # 行数
        is_sorted = False
        for j in range(0, sort_border):  # 每一行交换的次数
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
                last_exchange_index = j
                is_sorted = True
        sort_border = last_exchange_index
        print(f"第{i}轮排序后 表现为{list1}")
        if is_sorted == False:
            break
    return list1
print(bubbleSort_v3([2, 3, 1, 9, 12,43,45]))

"""
实例方法  定义方法的第一个参数为self
类方法  定义方法的第一个参数为cls 并且使用装饰器@classmethod
静态方法  定义方法没有 self cls 使用装饰器@staticmethod
"""


class Func_demo:

    def instance_func(self):
        print("这就是实例方法")

    @classmethod
    def class_func(cls):
        print("这是类方法")

    @staticmethod
    def static_func():
        print("这是静态方法")

func = Func_demo()
# print(func.instance_func()) # 实例对象调用静态/实例/类方法
# print(func.class_func())
# print(func.static_func())



Func_demo.class_func() # 类对象调用 类方法、静态方法
#Func_demo.instance_func()
Func_demo.static_func()

# 归属
# print(func.instance_func) # 实例对象调用静态/实例/类方法
# print(func.class_func)
# print(func.static_func)

# 使用场景
# 静态方法 无法访问类属性和实例属性
# 类方法 只涉及使用类变量的方法
class Car:
    max_speed = 260

    # @classmethod
    # def modify_speed(cls, speed):
    #     cls.max_speed = speed

    # 当类变量是不可变对象时 实例变量对类变量赋值、而是在给该实例对象创建新的属性、即修改类变量相当于给这个实例新增一个属性
    def modify_speed(cls, speed):
        cls.max_speed = speed

car1 = Car()
car2 = Car()
car1.modify_speed(380)
# print(car1.max_speed)
# print(Car.max_speed)
# print(car2.max_speed)

# python 魔术方法 自动调用 不需要手动调用
# 通过重写魔术方法 修改魔术方法原本要实现功能的判断规则

class Student:
     def __init__(self,name,score):
         self.name = name
         self.score = score

     # __equal__
     def __eq__(self, other):
        return self.score == other.score

# > __gt__  >= __ge__ < __lt__  <= __le__ ! __ne__


s1 = Student('kp',90)
s2 = Student('cc',90)
print(s1 == s2)
print(3==5)


# __new__ 实例化对象调用第一个方法

class Dog:
    # 初始化的过程 实例级别的
    def __init__(self, name, score):
        print("__init__called")
        self.name = name   # 在给实例赋值时会先调用__setattr__ 并且将属性名字和属性值添加到__getattr__方法中
        self.score = score

   # 控制生成一个实例的过程 类级别的
    def __new__(cls, name, age):
        print("__new__called")
        return super(Dog, cls).__new__(cls) # 返回一个dog实例

    # __str__定制化输出  __repr__
    def __str__(self):
        return f'这是一只叫{self.name}的狗--str'
   # 系统会默认先找__str__方法、如果没有，则会找_repr__
    # 如果都找不到会使用默认展示
    # 交互模式 会优先调用repr方法
    def __repr__(self):
        return f'这是一只叫{self.name}的狗--repr'

    # 当访问类的实例属性不存在时、使用该方法定制化错误输出
    def __getattr__(self, item):
        print(f'no {item}')

    # #
    # def __setattr__(self, key, value):
    #     pass


dog = Dog("小黑", 10)  #
print(dog.foot)
# print(Dog.__dict__)  # 输出该类的属性的字典
print(dog.__dict__)  #
# 单态(单例)
# 在整个程序运行过程中，一个类只有一个实例


class Singleobject():
    # 类变量
    instance = None
   # 控制实例的产生过程
    def __new__(cls):
        # hasattr(object,name) 用于判断对象是否包含对应的属性
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleobject, cls).__new__(cls)
        return cls.instance
        # if not cls.instance:
        #     cls.instance = super(Singleobject, cls).__new__(cls)
        # cls.instance

# if __name__ == "__main__":
#     print("实例化对象1")
#     s1 = Singleobject()
#     print("实例化对象2")
#     s2 = Singleobject()
#     print(id(s1))
#     print(id(s2))


class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, key, value):
        print("*"*30)
        print(f'setting key is {key}, value is {value}')
        print(f'current __dict__ is {self.__dict__}')
        self.__dict__[key] = value

    # 返回对象的属性的长度
    def __len__(self):
        return len(self.name)


a1 = Animal('dog', 10)

print(len(a1))

# 对象之间的运算：+ :__add__ -:__sub__  * __mul__  / __truediv__  // __floordiv__  % __mod__
class Vector:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'vector({self.x},{self.y})'

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)



v1 = Vector(1, 2)
v2 = Vector(5, 6)
print(v1 + v2)


# 异常处理
def div():
    try:
        1/0
        print(11)
    except (ZeroDivisionError, ValueError): # 可以写多种异常
        print("抓取到了被除数为0")
    else:
        print("整个程序一切正常、不跑异常走这里")
    finally:
        print("不管有没有异常都会执行这里")




div()