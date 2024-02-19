"""
变量命名规则
第一个字符不为数字
只能为 字母 数字 _ 的组合
不能使用关键字
"""
# 创建一个内存空间 b 指向了 'ccc'
a= 'ccc'
b = a
a = 'ddd'
print(b)

"""
1、可以包含不同类型的元素
2、序列中可以包含序列
3、可以通过索引访问其中的元素
4、序列的操作：+ *  判断成员资格 求长苏 最大/最小值
"""
a = (1,2,3,4)
b = (9,0)
print(a+b)

name = 'kj'
money = 100
s = '亲爱的%s 你的余额还有%d'
s1 = f'{name} 你的余额还有{money}'
s2 = '亲爱的{} 你的余额还有{}'.format(name, money)

s1 = 'xfdf sfsdf dsfsf'
s1.title()
print(s1.capitalize())


# 整体reverse
# 单个分割 然后reverse
s11 = 'i am a boy'
s112 = s11.split()
s12 = s112[::-1]
print(' '.join(s12))



a = 'sdadadfa'
dict1 = {}
# for i in a:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
# print(dict1)
#
# for i in a:
#     dict1[i] = dict1.get(i, 0)+1
# print(dict1)
# # 分支简略写法 三元运算符
# a = 3
# b = 5
# 'xxx' if a >b else 'uui'
#
# {True:'xxx',False:'YYY'}[a>b]
#
# '-5到256  常量池 缓存 不会开拓新的空间'
# a = 256
# b = 256
# print(a is b)
# a = 257
# b = 257
# print(a is b)  # 返回False
#
# a = [2,5,7]
# aa = [i+1 for i in a]
# print(aa)
#
# a = 10
# b = 5
# try:
#     result = a/b
# except:
#     print('exception')
# finally:
#     print('ok')  # 无论如何都会执行


# 捕获多种异常

# try:
#     result = a/b
# # except(ValueError, IndexError):
# #     print('')
# except ValueError:
#     print('exception')
# except TypeError:
#     print('类型粗偶')
# finally:  # 无论如何都会执行
#     print('ok')
# from random import randint
# def test():
#     player_choice = input('请输入你的手势')
#     if player_choice == None:
#         return '未输入'
#     a = {'石头': 1, '剪刀': 2, '布': 3}
#     num1 = randint(1, 3)
#     print(num1)
#     if a[player_choice] > num1:
#         return "winner"
#     elif a[player_choice] < num1:
#         return 'loser'
#     else:
#         return '平局'
# print(test())


# def test():
#     player_choice = input('请输入你的手势')
#     if player_choice == None:
#         return '未输入'
#     a = {'石头': 1, '剪刀': 2, '布': 3}
#     num1 = randint(1, 3)
#     print(num1)
#     if a[player_choice] > num1:
#         return "winner"
#     elif a[player_choice] < num1:
#         return 'loser'
#     else:
#         return '平局'
# print(test())

def func(*nums):
    print(type(nums)) # y元组

def func1(**kwargs):
    return kwargs# 字典

dict12 = {'x':1, 'b':2}

print(func1(**{'x':1, 'b':2}))
print(func1(a=1,b=2))



