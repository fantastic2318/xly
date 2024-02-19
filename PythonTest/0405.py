# 循环
# 遍历字符串
# 遍历字典
# break continue
# for/while + else  整个循环能都正常结束 就会执行else
# nums = [1,2,3,4,5,6,7]
# for i in nums:
#     print(i)
# else:
#     print("所有元素都正常打印")
# # 结束某次循环、else会执行
# for i in nums:
#     if i == 4:
#         continue
#     print(i)
# else:
#     print("所有元素都正常打印")
# # 提前结束整个循环、else没有执行
# for i in nums:
#     if i == 4:
#         break
#     print(i)
# else:
#     print("所有元素都正常打印")


# ['a', 'b', 'c'] ---> ['A', 'B', 'C']
a = ['a', 'b', 'c']
b = []
for i in a:
    b.append(i.upper())
print(b)
# 列表推导式
"""
[out_exp_res for out_exp in input_list if XXXX]
[输出表达式 for 变量 in 变量范围 if变量在范围内的取值条件]
out_exp_res 可以是表达式 也可以是函数
"""

def fun(i):
    return i *3

b = [i.upper() for i in a]
print(b)

nums = [1,2,3,4,5,6]  # -->[3,4,5,6,7,8]
# out_exp_res 可以是表达式
nums2 = [i+2 for i in nums]
print(nums2)
# 只对奇数处理
nums3 = [i+2 for i in nums if i % 2 != 0]
print(nums3)
# out_exp_res 可以是函数
nums4 = [fun(i) for i in nums if i % 2 != 0 ]
print(nums4)

# 元组推导式--不可以（元组是不可变对象）
# 字典推导式
# set推导式

# 函数
"""
函数：是组织好的 可重复使用 用来实现某些特定功能的代码块
参数 调用函数时 提供给函数的值
"""

def func():
    print("say hi")
print(func) # 函数名 表示 函数名变量 指向的函数对象
print(func()) # 函数名() 表示 调用函数

# pass
def func(name):
    print(f'hi{name} ,how are you')
    # 这是方法 但是还没实现
    pass

# 给函数写注释
def func_1():
    """
    this is note
    :return:
    """
    pass
# 通过函数的内置方法 打印注释
print(func_1.__doc__)

# 参数
# 位置参数 严格按照参数的顺序来读取 调用函数的时候传入的参数和定义的函数位置完全对应
# 可以在调用的时候 传入参数值加上参数名
def hello(name,age):
    print(f'my name is {name} i am {age} years old')

hello(age=20,name='kunp')
# 非关键参数一定要放在关键参数前(没有指定参数名参数 放在指定参数前面)
# hello(age=20,'kunp')
hello('kunp',age=20)

# 默认参数  定义函数时 给定传入参数的默认值 在调用函数时 可以不提供参数/部分提供/全部提供
# def hello_country(greeting,country):
#     print(f'{greeting}, I come from {country}')

def hello_country(greeting='hi',country='Japan'):
    print(f'{greeting}, I come from {country}')
hello_country('good_morning','China')
hello_country(country='USA')
# 默认参数一定要在位置参数后

# 可变参数 *arg 把传进来的0或者N个参数组装成一个元组
# members = ['cc','xiaoniu']
# def greeting(greet,members):
#     for m in members:
#         print(f'{greet}:{m}')
# greeting('hi',members)
#members = ['cc','xiaoniu']
def greeting(greet,*members):
    print(type(members)) # tuple
    for m in members:
        print(f'{greet}:{m}')
greeting('hi','cc','kunp','xiaoniu')

# 关键字参数   **kwarg  传入任意个带参数名的参数  会自动组装成一个字典
def print_person(name,male,**kwargs):
    print(type(kwargs))
    print(f'my name is {name},I am a {male}, other information is {kwargs}')

print_person('k','M',age=20,nation='china')

# 参数组合：位置参数 默认参数 可变参数 关键字参数

# 函数作用域
"""
函数内部定义的变量  局部作用域Local
全局变量（函数外）--》 全局作用域（整个py文件）global
enclosing 函数内部与嵌套函数之间的作用域
building-in 内置作用域

L -->E -->G --B
"""
# 修改全局变量 global
print("*"*20)
x = 1
def changex_gloal():
    global x
    x += 2
    return x
print(changex_gloal())
print("*"*20)
# 函数可以嵌套函数
passline = 60
def func(val):
    passline=90          #
    if val >= passline:
        print("pass")
    else:
        print("fail")
    def inner_func():  # 先找Local 找不到再找enclosing
        nonlocal val  # nonlocal 非local 定义变量后 可以修改enclosing中其他外层函数的中定义的局部变量
        val += 3
        print(val)
    return inner_func()

print(func(89))

def get_Max(v1, v2):
    return max(v1, v2)

# 匿名函数
# lambda x, y: x-y
# func 接收两个参数 x,y 返回x-y
def xx(x,y):
    return x-y
func = lambda x, y: x-y  # 将匿名函数对象赋值给func
func(9, 1)

# 函数的特性
# 1、函数可以作为一个变量赋值给另一个变量
def addd(x):
    return x+1
a = addd
print(a)
print(a(5))
# 2、函数可以作为参数
def excute(f):
    return f(5)

print(excute(addd)) # 函数作为参数

# 函数可以作为返回值
def get_add():
    return addd # 返回函数对象
c = get_add()
print(c)

# 闭包  是由函数及其相关的引用组合而成的实体
"""
如果在一个内部函数里，对外部作用域（不是全局作用域）的变量进行引用，内部函数就是闭包closure
1、函数嵌套函数（嵌套函数）
2、包含对外部作用域而非全局作用域的引用
实现了闭包函数 叫闭包函数 通常会返回一个值

# 调用外层函数时 运行到def内部时，仅仅是完成对函数的定义 而不会去调用内层函数
# 函数内部的作用域 在函数调用结束后 会被清除掉 enclosing作用域 在嵌套函数返回之后仍然有效
"""
# 不是闭包、因为不符合第二条
x = 1
def outer_1():
    def inner():
        print(f"this is inner,param is {x}")
    inner()
    print('this is outer')
outer_1()
# 是闭包
def outer_2():
    x = 1
    def inner():
        print(f'this is inner，param is {x}')
    inner()
    print('this is outer')
outer_2()

# 装饰器
import time
from random import randint

def wrapper(func):
    def inner():
        startTime = time.time()
        func()
        endTime = time.time()
        print(endTime -startTime)
    return inner

# 装饰器无参
@wrapper
def func_sleep():
    sleep_time = randint(0,3)
    time.sleep(sleep_time)
    print("hahah")

func_sleep()
print(func_sleep)  # <function wrapper.<locals>.inner at 0x7f867f6073a0>

# 装饰器装饰有参数的函数
def wrapper1(func):
    def inner(a,b):
        startTime = time.time()
        s = func(a,b)
        endTime = time.time()
        print(endTime -startTime)
        return s
    return inner

@wrapper1
def func_sleep1(a,b):
    sleep_time = randint(0,3)
    time.sleep(sleep_time)
    return a+b

print(func_sleep1(3,5))

# 装饰器本身有参数
def outer_wrapper(str1):
    def wrapper1(func):
        def inner(a, b):
            if str1 == "测试1":
                startTime = time.time()
                s = func(a, b)
                endTime = time.time()
                print(endTime - startTime)
            return s
        return inner
    return wrapper1
# 为了满足多种情况的装饰时使用
@outer_wrapper("测试1")
def func_sleep3(a,b):
    sleep_time = randint(0,3)
    time.sleep(sleep_time)
    return a+b

print(func_sleep3(5,7))

# 有多个装饰器的执行顺序  由内而外执行， 距离近的装饰器先执行、被装饰函数的执行顺序：最远的先执行
# 对类进行装饰




