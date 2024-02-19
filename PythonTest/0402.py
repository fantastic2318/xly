# 字符串查找 作业
# count find
# find 查找、返回从左边第一个指定字符的索引、找不到返回-1 rfind
a = "i love you"
print(a.find('i', 1))

# 字符串的修饰
'''
****aa****
aa********
*******aa
'''
str1 = '   aa1   '
print(str1.center(10, '*'))  #  总宽度  剩下的以'*'填充
print(str1.ljust(10,'-')) # 左对齐
print(str1.rjust(10, '~')) # 右对齐
print(str1.zfill(10)) # 跟右对齐效果一致、只是默认用0填充
print(str1.rstrip()) # lstrip 默认去掉左边空格 strip 默认去掉空格
print(str1.replace('1', ''))

# 大小写转化
'''
upper() 小写变大写
lower()  大写变小写
title()  单词首字母大写 其他字母小写
captialize() 字符的首字母大写
swapcase() 字符的大小写转化
'''
str2 = 'i am a girl'
# 大小写相互转换
str3 = str2.title()
print(str3.swapcase())
print(str3.capitalize())

# 字符串判定
'''
isalnum  数字+字母 组成
isdigit  数字
isalpha  字母
isspace  全部都由空格组成
isupper  全部是大写  只判断字母 不判断数字
islower 全部都是小写  只判断字母 不判断数字
starstwith 以。。开始
endswith  以。。  结束
'''

str4 = 'abd2321uoiuh'
print(str4.isalnum())
print(str4.islower())  # 只判断字母 不判断数字 返回true
print(str4.startswith('a', 1, 5)) #  是否以a开头 查找范围index1-5  查找范围可以缺省
print(str4.endswith('i', 1, 10))  # endswith 左闭右开 1-10返回true 1-9返回False

# 字典
'''
map key-value  不是序列
'''
# 1、直接定义
namebook = {'kump':'12344243', 'niu':'323232'}

# 2、dict()类型函数  key 是不可变 字符串 元组 数字不可变类型
items = [('k', '2323'), ('o', '2334')]
namebpook = dict(items)
dict1 = dict(lup='23232', new='231231')
print(dict1['lup'])
dic2 = {(2, 3): 'key 是元组'}
dic3 = {2: 'key 是数字'}
person = {'age':10, 'age':11}  # 如果两个key相同、则按照顺序、使用最后一个value
print(person['age'])

# dict的操作
person = {'age':10, 'Weight':150}
person['age'] = 90
# 访问一个不存在的key 会报错
# 若键不在字典中、则自动添加字典
person['height'] = 180
print(person)

# del 删除key
del person['Weight']
# 返回字段长度
print(len(person))

# 判断 键是否存在字典中
print('name' in person)

# 字符格式化
person = {'name': 'zhagnsan', 'age': 20}
str5 = 'hello %(name)s you are %(age)d years old' % person
print(str5)

# 字典常用方法
# 1.clear  返回None
person1 = {'name': 'zhagnsan', 'age': 20}
person1.clear()

# copy()  浅拷贝 只复制对象本身简单对象 当子序列为可变对象 子序列改变会影响原对象
person1 = person.copy()
print(person1)

person1['age'] = 30
print(person1)  # 30
print(person)  # 20

# deepcopy 深复制 复制对象及其子对象 当子对象是可变对象时 子对象改变 不会影响原对象
# p1 = {'name': 'zhagnsan', 'age': 20, 'hobiits':['football', 'tennis']}
# from copy import deepcopy
# p2 = deepcopy(p1)
# p2['hobiits'].append('basketball')
# print(p1)
# print(p2)

# fromkeys 使用给定的键 建立新的字典 每个键默认的值对应的None
dict23 = {}.fromkeys(['name', 'age'])
print(type(dict1), dict1)

# get 比较宽松，如果key不存在返回None
print(person1['name'])
print(person1.get('name'))
print(person1.get('sex'))
# 字典get方法找不到key 将会设置默认值0 get(i,0)
for i in a:
    dict1[i] = dict1.get(i, 0)+1
print(dict1)

# items 将字典中的多有项 以列表方式返回、其中每一项都会表现为{key,value}的形式返回
print(type(person1.items()), list(person1.items()))

# keys() values() 同上
# 判断key是否存在字典中
print('age' in person1)
# pop()删除指定键值对
# person1.pop('name')
# print(person1)
# 删除最后一组键值对
person1.popitem()
print(person1)

# update 利用一个字典 更新另一个字典 会添加到原字典中
x = {'sex': 'M', 'age': 20}
person1.update(x)
print(person1)

# setdefault key存在 返回對應的值 key不存在 返回的是插入的值  并且把键值对插入
d = {}
print(d.setdefault('sex', 'F'))
print(d)
#person1.setdefault('sex', 'F')
#print(person1)

sorce = {'java': 90, 'python': 97, 'C#': 89}
'''
1、求字典的长度
2.修改Java的成绩--》95
3.增减一项 php 90
4.判断js 在不在字典中
5.获取字典中的最好成绩
'''
len(sorce)
sorce['java'] = 95
sorce.setdefault('php', 90)
print('js' in sorce)
print(max(sorce.values()))

def key():
    sorce = {'java': 90, 'python': 97, 'C#': 89}
    for k,v in sorce.items():
        if v == max(sorce.values()):
            print(k)
key()

# 集合 set
'''
集合 一个无序的 不重复元素的组合
'''
# 定义集合
# 1、set()
s1 = set('abs')
s2 = set(['a', 'b', 'c'])
print(type(s2), s2)
s3 = set(('a','b','c'))
# s4 = set(123) # 参数必须是可迭代对象

# 2、直接定义
s5 = {1, 2, 3}
print(type(s5), s5)
# 定义空集合
s6 = set('')

# 集合方法
# 添加
set1 = set('abc')
set1.add('f')
set1.remove('b')
# set1.remove('r')# 删除一个不存在的元素 报错
# update 会把传入的元素拆分
set1. update('oiou')
print(set1)

'''
list1 = [1,2,3,5,6,3,2]
list2 = [2,5,7,9]
1。哪些数同时在list1 和list2
2、哪些数在list1中 不在list2中
'''
def and1234(list1,list2):
    d1 = dict()
    lis1 = set(list1)
    for i in lis1:
        if d1.get(i) == None:
            d1[i] = 0

    for k, v in d1.items():
        if k in list2:
            d1[k] += 1
    return d1

print(and1234([1,2,3,5,6,3,2],[2,5,7,9]))

# 集合操作符
'''
& 交集
| 合集 并集
- 差集 相互补集
'''
list1 = [1,2,3,5,6,3,2]
list2 = [2,5,7,9]
s1 = set(list1)
s2 = set(list2)
print(s1&s2)
print(s1|s2)
print(s1-s2)

# 序列解包
# 赋值语法糖
a, b, c = 1, 2, 3
# a,b = b,a  两值互换语法糖
values = 1, 2, 3  # type(values) tuple
x, y, z = values  # 左右元素个数必须相同
colors = ['red', 'green', 'blue', 'black', 'white']
# *other表示除了 C1 C2外 其他元素再次打包给other
c1, c2, *other = colors
print(c1, c2, other)
# 字典序列解包得到key值
dict3 = {'name': 'zhagnsan', 'age': 20, 'weight':60}
x,y,z = dict3
print(x,y,z)

a = b = 1
b = 2
print(a) #  a = 1

# 数字运算的时候 True False 分别代表 1,0
print(True+False+20) # 21

# '', [], 0, ()
print(bool)

a,b = 3,2
# c = 'more' if a>b else 'less'
print(c)

c = {True:'more',False:'less'}[a>b]
print(c)

# 赋值
'''
and 偶or not
is  is not
'''
x = 1
y = 1
print(x == y)
print(x is y)
print(id(x),id(y)) # 查看内存地址
