# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# # def print_hi(name):
# #     # Use a breakpoint in the code line below to debug your script.
# #     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# # if __name__ == '__main__':
# #     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# # def testFunc():
# #     #str1.split(";")
# #     return 3 == 2
# #
# # print(testFunc())
#
# # s = "abcdefg"
# # print(s[1:4])
#
# # myDict = {"name": "Bill", "country": "USA"}
# # mySeparator = "TEST"
# #
# # x = mySeparator.join(myDict)
# #
# # print(x)
# # #
# # dir = '','usr','bin','env'
# # print('/'.join(dir))
#
# # d = [{"a": 9}, {"b": 2}, {"d":5}]
# # d.sort(key=lambda x: list(x.values())[0])
# # print(d)
# #
# # print()
# #
# # a = [0,1,2,3,4,5,6,7,8,9]
# # print(a[:6:-1])
#
#
#
#
# # s = [1,2,3,4,5]
# # # s.__getitem__()
# # # s.__iter__()
# #
# # # 如何判断一个对象是可迭代对象
# # from collections.abc import Iterable
# # isinstance("abc", Iterable)
#
#
# #列表生成式
#
# # list1 = [x * x for x in range(0,4)]
# # print(list1)
# #
# #
# #
# # list2 = [x * x for x in range(0,4) if x % 2 == 0]
# # print(list2)
# #
# # list3 = [m + n for m in 'ABC' for n in 'XYZ']
# # #['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
# # print(list3)
#
# #
# # list9 = [0 for m in range(2) for n in range(3)]
# # print(list9)
# #
# # d = {'x': 'A', 'y': 'B', 'z': 'C' }
# # list4 = [k + '=' + v for k, v in d.items()]
# #
# # print(list4)
# #
# # L = ['Hello', 'World', 'IBM', 'Apple']
# # list5 = [s.lower() for s in L]
# #
# #
# # list6 = [x if x % 2 == 0 else -x for x in range(1, 11)]
#
#
# # def triangles():
# #     n = [1]
# #     while True:
# #         yield n
# #         n = [x + y for x, y in zip([0] + n, n + [0])]
# #
# #
# # n = 0
# # for t in triangles():
# #     print(t)
# #     n = n + 1
# #     if n == 10:
# #         break
#
#
# # def triangles():
# #     L = [1]  # 定义L为一个只包含一个元素的列表
# #     while True:
# #         yield L  # 定义为生成器函数
# #         L = [1] + [L[n] + L[n - 1] for n in range(1, len(L))] + [1]
# #
# #
# # n = 0
# # for t in triangles():
# #     print(t)
# #     n = n + 1
# #     if n == 10:
# #         break
#
# # L = [1]
# # print(L[1] + L[1])
# # from functools import reduce
# #
# #
# # r = reduce(lambda x, y: x + y, [1])
# #
# # # print(r)
# # s = [0,0,0,0,0,0,0,0]
# # index2 = 5
# # s[index2-2: index2+1] = ["%","2","0"]
# # print(s)
# #
# #
# # def odd():
# #     pass
# #
# # a = list[filter(odd(),range(10))]
# # print(a)
#
#
#
# # def fib(max):
# #     n, a, b = 0, 0, 1
# #     while n < max:
# #         yield b
# #         a, b = b, a+b
# #         n = n + 1
#
#
# # def odd_iter():
# #     n = 1
# #     while True:
# #         n += 2
# #         yield n
# #
# # def not_div(n):
# #     return lambda x: x % n > 0
# #
# # def primes():
# #     yield 2
# #     it = odd_iter()
# #     while True:
# #         n = next(it)
# #         yield n
# #         it = filter(not_div(n), it)
#
#
# # p = primes()
# # for i in p:
# #     if i < 10:
# #         print(i)
# #     else:
# #         break
#
#
# # # 闭包
# # def outFunc(*args):
# #     def innnerFunc():
# #         x = 0
# #         for n in args:
# #             x += n
# #         return x
# #     return innnerFunc
# #
# #
# # o = outFunc(1,2,3,4,5)
# # print(o())
# #
# #
# # def create(pos=[0, 0]):
# #     def go(direction, step):
# #         new_x = pos[0] + direction[0] * step
# #         new_y = pos[1] + direction[1] * step
# #
# #         pos[0] = new_x
# #         pos[1] = new_y
# #
# #         return pos
# #
# #     return go
# #
# #
# # player = create()
# # print(player([1, 0], 10))
# # print(player([0, 1], 20))
# # print(player([-1, 0], 10))
#
#
# # def outer_fun():
# #     x = 0
# #
# #     def inner_fun():
# #         x = 1
# #         print('inner x:', x, 'at', id(x))
# #
# #     print('outer x before call inner:', x, 'at', id(x))
# #     inner_fun()
# #     print('outer x before call inner:', x, 'at', id(x))
# #
# #
# # outer_fun()
# #
# #
# # def outer_fun():
# #     x = 0
# #
# #     def inner_fun():
# #         nonlocal x  # 注意这里
# #         x = 1
# #         print('inner x:', x, 'at', id(x))
# #
# #     print('outer x before call inner:', x, 'at', id(x))
# #     inner_fun()
# #     print('outer x before call inner:', x, 'at', id(x))
# #
# #
# # outer_fun()
#
# #
# # def inc():
# #     x = 0
# #     def fn():
# #         #nonlocal x  # 证明该变量不是内层函数的局部变量
# #         return x+1
# #     return fn
# #
# # f = inc()
# # print(f()) # 1
# # print(f()) # 2
#
#
#
# # # 装饰器不带参数
# # def log(func):
# #     @functools.wraps(func)
# #     def deco(*args, **kwargs):
# #         print("call %s():" % func.__name__)
# #         return func(*args, **kwargs)
# #     return deco
# #
# # # now = log(now)
# # #
# # # now()
# #
# #
# # @log
# # def now():
# #     print("2022-10-11")
# #
# #
# # now()
# #
# #
# #
# # # 装饰器带参数
# #
# # import datetime
# # import functools
# #
# #
# # def log(paramter):
# #     def outerdeco(func):
# #         @functools.wraps(func)
# #         def deco(*args, **kwargs):
# #             print("%s %s():" % (paramter, func.__name__))
# #             # timer = func(*args, **kwargs)
# #             # return timer
# #             return func(*args, **kwargs)
# #         return deco
# #     return outerdeco
# #
# # # now = log(now)
# # #
# # # now()
# #
# #
# # @log("execute")
# # def now():
# #     print("2022-10-11")
# #     return datetime.datetime.now()
# #
# #
# # #print(now())
# # print(now.__name__)
#
# from collections import deque
#
# from functools import reduce
#
# from datetime import datetime
#
# import hashlib
#
# import base64
#
# import urllib
#
# import contextlib
#
# import itertools
#
# from copy import copy
#
# from copy import deepcopy
#
# import pathlib
#
#
# # a = 5
# # b = 7
# # c = 5
# # print(id(a))
# # a = 9
# # print(id(a))
# #
# # print(id(b))
# # print(id(c))
# #
# #
# # list1 = [1,2,34]
# # print(id(list1))
# # list1.append(9)
# # list2 = [1,2,34]
# #
# # print(id(list1))
# # print(id(list2))
# # print(list1 == list2)
#
#
# # list1 = [1,2,34, 8]
# # list4 = list1
# # list4.append(4)
# # print(id(list1))
# # print(id(list4))
#
#
#
# # import heapq
# #
# # elm = [4,5,2,1,7,3,2,0,6,8,2]
# #
# # heapq.heapify(elm)
# #
# # print(elm)
# #
# # heapq.heappush(elm, 999)
# #
# # print(elm)
# #
# # heapq.heappop(elm)
# #
# # print(elm)
# #
# # heapq.heapreplace(elm, 9)
# #
# # print(elm)
# #
# # res = heapq.nlargest(3, elm)
# #
# # print(res)
# #
# # res1 = heapq.nsmallest(2, elm)
# #
# # print(res1)
#
#
#
# # list1 = [1,2,3,4]
# # def solution(list1):
# #     list1 = [1,2,3,4,5]
# #     return list1
# # print(solution(list1))
# # print(list1)      # [1,2,3,4]
#
# #
# # list1 = [1,2,3,4]
# # def solution(list1):
# #     list1.append(5)
# #     return list1
# # print(solution(list1))
# # print(list1)
#
#
# import copy
#
# # strr = "abc"
# # ll = [1,2,3]
# # print("strr的地址{}".format(id(strr)))
# # print("ll的地址{}".format(id(ll)))
# #
# # print("----原始对象分割线----")
# # strr1 = copy.copy(strr)
# # lx = copy.copy(ll)
# # print("strr1的地址{}".format(id(strr1)))
# # print("lx的地址{}".format(id(lx)))
# # print("strr是strr1{}".format(strr is strr1))
# # print("lx是ll{}".format(lx is ll))
# # print("----修改前后copy分割线---")
# # strr1 = "abcd"
# # lx.append(9)
# # print("strr1的地址{}".format(id(strr1)))
# # print("strr的地址{}".format(id(strr)))
# # print("lx的地址{}".format(id(lx)))
# # print("strr是strr1{}".format(strr is strr1))
# # print("lx是ll{}".format(lx is ll))
# #
# # print("----深浅拷贝分割线----")
# # strr2 = copy.deepcopy(strr)
# # ly = copy.deepcopy(ll)
# #
# # print("strr2的地址{}".format(id(strr1)))
# # print("ly的地址{}".format(id(ly)))
# # print("strr是strr2{}".format(strr is strr2))
# # print("ly是ll{}".format(ly is ll))
# #
# # print("----修改前后deepcopy分割线---")
# # strr2 = "abcd"
# # ly.append(9)
# # print("strr2的地址{}".format(id(strr1)))
# # print("ly的地址{}".format(id(ly)))
# # print("strr是strr2{}".format(strr is strr2))
# # print("ly是ll{}".format(ly is ll))
#
#
#
# strr = [[1,2,3],"str"]
# print("strr的地址{}".format(id(strr)))
# print("strr1[0]的地址{}".format(id(strr[0])))
# print("strr1[1]的地址{}".format(id(strr[1])))
#
#
# print("----原始对象分割线----")
# strr1 = copy.copy(strr)
# print("strr1的地址{}".format(id(strr1)))
# print("strr1[0]的地址{}".format(id(strr1[0])))
# print("strr1[1]的地址{}".format(id(strr1[1])))
#
# print("----修改前后copy分割线---")
# strr1 = [[1,2,3,4],"str1"]
# print("strr1的地址{}".format(id(strr1)))
# print("strr1[0]的地址{}".format(id(strr1[0])))
# print("strr1[1]的地址{}".format(id(strr1[1])))
# print("strr的值{}".format(strr))
#
# print("----深浅拷贝分割线----")
# strr2 = copy.deepcopy(strr)
# print("strr2的地址{}".format(id(strr1)))
# print("strr2[0]的地址{}".format(id(strr2[0])))
# print("strr2[1]的地址{}".format(id(strr2[1])))
#
# print("----修改前后deepcopy分割线---")
# strr2 = [[1,2,3,4],"str1"]
# print("strr2的地址{}".format(id(strr1)))
# print("strr2[0]的地址{}".format(id(strr2[0])))
# print("strr2[1]的地址{}".format(id(strr2[1])))
# print("strr的值{}".format(strr))
#
#
#
#
# map = {
#     "header": "id",
#     "payloads": {
#         "id": 1
#     },
#        }
#
#
# tuple1 = ([1,2,3],1)
#
# def test(map, t):
#     map = copy.deepcopy(map)
#     t = copy.deepcopy(t)
#     map["payloads"]["id"] = 2
#     print(map)
#     t[0].append(6)
#     print(t)
#
# test(map, tuple1)
# print(map)
# print(tuple1)
#
#
#
# def test1(map, t):
#     map = copy.copy(map)
#     t = copy.copy(t)
#     map["payloads"]["id"] = 2
#     print(map)
#     t[0].append(6)
#     print(t)
#
# test1(map, tuple1)
# print(map)
# print(tuple1)

# s = "abcdrftyui"
# print(id(s))
#
# s = s[0:-1]
# print(id(s[0:-1]))
# print(s)
# print(id(s))
#
#
#
# ll = ["a", "b", "c"]
# print(id(ll))
#
# ll = ll[0:-1]
# print(id(ll[0:-1]))
# print(ll)
# print(id(ll))


"""读写文件"""
import json
import ast
# file = open(file='hello.txt', mode='r', encoding='utf-8')
# con = file.readline()
# print(con)
# with open(file='hello.txt', mode='r', encoding='utf-8') as f:
#     print(f.readlines())
# sum_time = 0
# count = 0
# for line in open(file='hello.txt', mode='r', encoding='utf-8').readlines():
#     json_1 = ast.literal_eval(line)
#     sum_time += int(json.loads(json_1)["age"])
#     count += 1
# print(sum_time/count)


# with open("hello.txt", 'r', encoding='utf-8', newline='\n') as f:
#     for line in f:
#         #print(line.strip('\n'))
#         json_1 = ast.literal_eval(line.strip('\n'))
#         sum_time += int(json.loads(json_1)["age"])
#         count += 1
# print(sum_time/count)


# with open('hello.txt', 'r') as f:
#     for line in f:
#         print(line.strip('/n'))

#
# for line in open(file='hello.txt', mode='r', encoding='utf-8').readlines():
#     print(type(json.loads(line)))


# import json
# a = '{"name" : "john", "gender" : "male", "age": 28}'
# c=json.loads(a)
# print(c, type(c))

def quickSort(left, right, nums):
    if left > right:
        return None
    tmp = nums[left]
    i = left
    j = right
    while i != j:
        while nums[j] >= tmp and i < j:
            j -= 1
        if i < j:
            nums[i] = nums[j]
            i += 1
        while i < j and nums[i] <= tmp:
            i += 1
        if i < j:
            nums[j] = nums[i]
            j -= 1
        nums[i] = tmp
    quickSort(left, i-1, nums)
    quickSort(i+1, right, nums)
    return nums

print(quickSort(0,9,[1,5,2,4,-1,9,7,6,3,10]))