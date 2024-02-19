"""
1.实现⼀一个装饰器器，每次调⽤用函数时，将函数名字 和 调⽤用时间写入到 文件 a.txt 中
tips:
要求先熟悉 python ⽂文件的操作 函数名可⽤ name 来获取 调用时间 可以熟悉 time 模块
"""
import time

def wrapper(func):
    def inner():
        ret = func()
        file = open('a.txt', 'w')
        for r in ret:
            file.write(r+'\n')
        file.close()
        return ret
    return inner

@wrapper
def function():
    return function.__name__, str(time.time()) # 文件名问题和文件读写问题

function()


"""
2.一个实验。如果你掷硬币100次，并在每次正⾯面时写下“H”,在每次 反⾯面时写下“T”，就会创建⼀一个看起来像“TTTHHTHTTHHHH”这样的列列表。
如 果你要求一个人进⾏100次随机掷硬币，你可能会得到正反交替的结果，
例 如“HHTTHTTTHHHT”。 
编写⼀一个程序，计算随机⽣成的正⾯和反列表中出现 连续6个正⾯面或者6个反⾯面的频率，重复实验1000次，检查出现连续6个正⾯面或 者反⾯面的实验次数，并计算出现的频率。
即 1000次实验中，每次回掷硬币100 次 ，然后判断 这 100次内是否有 连续6 次正⾯或 反⾯ 的情况
"""
from random import randint
def func():
    list1 = []
    str1 = ''
    for i in range(0, 100):
        x = randint(0, 1)
        # if x == 1:
        #     list1.append("H")
        # else:
        #     list1.append("T")
        res = "T" if x == 0 else "F"
        str1 += res# 用字符串
    return list1


def getQueue(list1):
    queue = []
    queue.append(list1[0])
    for i in list1[1:]:
        if len(queue) < 6 and queue[0] == i:
            queue.append(i)
        elif len(queue) < 6 and queue[0] != i:
            while len(queue) > 0:
                queue.pop(0)
            queue.append(i)
        elif len(queue) == 6:
            return "有"
    else:
        return "没有"


def guess():
    condition = []
    for i in range(0, 1000):
        list2 = func()
        h = getQueue(list2)
        condition.append(h)
    return condition

print(guess())


"""
3.假设一个游戏的⻆⾊ 装备如下 goods = ['gold coin','dagger','gold coin','gold coin','ruby',.......] ，
请写一个小程序，统计 他的装备，返回如下所 示: 3gold coin 1 rope 1 dagger 1 ruby Total number of item: 48
"""
from functools import reduce

def countGoods(goods):
    dict1 = dict()
    for i in goods:
        if i not in dict1:
            dict1[i] = dict1.get(i, 0) + 1
        else:
            dict1[i] += 1
    t = zip(dict1.values(), dict1.keys())
    s = list(reduce(lambda x, y: x+y, t))
    r = list(map(lambda s: str(s), s))
    totalStr = " ".join(r)
    totalCount = reduce(lambda x, y: x+y, dict1.values())
    return totalStr, totalCount


c = countGoods(['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'])
print(f'{c[0]} Total number of item: {c[1]}')

# 先去重  得到列表 然后遍历这个列表 看每个元素在是不是在字典中  字典是由 元素和元素个数的元组组成
for i in set(good_list):
    list1.append((i,good_list.count(i)))

dict(list1)


"""
4.实现冒泡排序
"""
def bubbleSort(list1):
    for i in range(len(list1)-1, -1, -1):
        for j in range(0, i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1

print(bubbleSort([20,23,1,43,12,9]))



"""
5.实现一个函数，该函数参数为任意数量的数字，在函数中实现这样
的功能:统计在参数中 出现的数字的个数
"""
def countNum(*args):
    return len(set(args))
print(countNum(12,4,5,6,7,8,0,9,0))

"""
6.利⽤⾯面试对象的编程思想，实现下面的功能 
b. 小明 体重 80kg
c. 每跑步⼀次 重量减去 0.5kg
d. 每吃⼀顿饭 重量增加 0.1kg
"""
import abc
class Person(metaclass=abc.ABCMeta):
    def __init__(self, weight):
        self.weight = weight

    @abc.abstractmethod
    def run(self,weight):
        weight -= 0.5

    @abc.abstractmethod
    def eat(self,weight):
        weight += 0.1

class XiaoMing(Person):
    def __init__(self, weight):
        super(XiaoMing, self).__init__(weight)

    def run(self, weight):
        weight -= 0.5
        return weight
    def eat(self, weight):
        weight += 0.1
        return weight


xiaoming = XiaoMing(67)
print(xiaoming.eat(67))
print(xiaoming.run(67))