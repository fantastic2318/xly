import sys
a = 'hello'
b = 1
print(sys.getsizeof(a))  # 变量指向对象在内存中占用大小
print(sys.getsizeof(b))
print(type(a))

"""
数字类型相互转化
通过类型函数来转化float() int() 精度会有变化
"""

# 取余 取模
print(5%2)
# 除法 得到浮点型
print(5/2)
# 整除 向下取整
print(5//2)   # 2
print(-5//2)  # -3
# 求幂
print(5**2)

"""
序列：一种数据结构，序列中的每一元素都会被分配一个序号（元素的位置）、也称为索引
从左往右  从0开始  从左往左 从-1开始

6种内置序列 字符串 元组 列表 buffer对象  xrange对象  Unicode字符串

"""
# 序列中可以包含任何元素
# 序列中可以包含其他序列
#
# 序列的操作
# 1、通过索引访问单个元素
a = ['a','b','c','d']
print(a[0],a[1],a[2],a[3])

print(a[-4],a[-3],a[-2],a[-1])

# 2、通过分片操作访问一定范围的元素 [startIndex：endIndex：step] 左闭右开-->endIndex值取不到
# 当分片索引中 起始索引 比 结束索引大  结果为空
# print(a[-1,-3]) # 结果为空
# print(a[-1,-3,-1]) # 结果为a[-2] a[-3]
# print(a[2:]) # 从2开始后的所有
# print(a[:])
# print(a[::2])
# print(a[::-1])

# 3.序列相加
# 只有两种相同类型的序列 '+' 合并为一个新的字符串
print([1,2,3]+['a',6,7])  #[1,2,3,'a',6,7]
print('abc'+'123')  # 'abc123'
#print([1,2,3]+'a,b,c')  # 报错

# 4、序列相乘-->多个序列相加
print([1,2,3]*3)

# 5、成员资格判断 判断元素是都存在序列中
str1 = 'hello'
print('w' in str1)
list1 = [1,2,3]
print(1 in list1)
# 6、长度 一般指元素的个数、最大值、最小值
print(len(list1))
print(min(list1))
print(max(list1))

print(len(str1))
print(min(str1))
print(max(str1))

# 列表
'''
可以随时添加或者删除其中的元素、可变类型
'''
#定义列表
a = [1,2,3]
print(type(a),a)
# 由list()函数生成，list()参数为一个可迭代对象
f = list('abc')

# 列表操作
# 查
a[0] = 5
# 删除
del a[1]
print(a)
# del a  删除整个列表
print(a) # 会报错 直接删除a

# 通过分片来删除
nums = [1,2,3,4,5]
nums[1:3] = []
print(nums)

# 通过分片来插入
name = list('hello')
print(name)
# 在3的位置插入'kunpeng' 不覆盖3后面的内容
#name[3:3] = list('kunpeng')  # ['h', 'e', 'l', 'k', 'u', 'n', 'p', 'e', 'n', 'g', 'l', 'o']
print(name)
# 在3的位置插入'hello' 覆盖3后面的内容
name[3:] = list('kunpeng')  # ['h', 'e', 'l', 'k', 'u', 'n', 'p', 'e', 'n', 'g']
print(name)

# 列表方法 增删改查(修改原列表的值)
# 增1、append(object) 返回None 直接修改原来的列表
list1.append(9)
list1.append([6,7])  #[1, 2, 3, 9, [6, 7]] # 追加的一个列表元素
print(list1)

# 增2.extend() 可以在列表末尾一次性追加另一个序列的多个值  返回值 None 修改了被扩展的列表
list1.extend([8,9])
print(list1) # [1, 2, 3, 9, [6, 7], 8, 9]  # 追加一个列表中的多个元素
list1.extend('abc')
# + 区别于 extend
# 1、可以让不同类型的序列连接成同一个列表2、+不改变原列表 返回新列表 extend 改变原列表 返回None
print(list1)

# 增3、insert() 将对象插入到列表指定的索引位置 返回None 修改原列表的值
'''
insert(index,object)
index 索引 把object 插入到这个索引之前
'''
list2 = [1,23,3,45,5]
list2.insert(1,90)
print(list2)

#查1.count() 统计某个元素在列表中出现的次数 不存在的返回0
nums = [1,2,1,[1,3]]
#print(nums.count(1))
#print(nums.count(3))

#查2、index() 从列表里直接找出一个匹配项的索引位置 找不到会报错
# print(nums.index(1)) # 不添加范围找
# print(nums.index(1, 2))  # 根据索引范围查找
# index(value,startIndex,endIndex)

#删1.pop() 移除列表中指定索引的元素、如果不指定索引、就删除最后一个元素、返回删除的元素值
# nums.pop()
# print(nums)
# nums.pop(-1)  # 删除队尾元素、出栈
# nums.pop(0)  # 删除队首元素、出队

# 删2、remove() 移除列表中的第一个匹配项、没有匹配项就报错 返回None 修改原列表
nums.remove(1)
print(nums)

# sort() 排序 修改原来列表值
nums2 = [2,3,4,1]
nums2.sort()  # key排序的依据 reverse=False
print(nums2)

# reverse() 将列表中的元素反向存放
nums.reverse()
print(nums)


info = [10, 20, 30, 40]
# info1 = info #  info Info1 指向同一块内存空间
info1 = info[:]  # info1 指向重新开辟一块内存空间
info1[1] = 50
print(info)

# 元组 Tuple
'''
序列的一种、逗号分割、不能修改元素(不可变类型)
'''
# 定义元组
# 1、() 直接定义产生
a = (1, 2)
a = (1,)  # 如果只有一个元素 需要加个逗号 否则无法定义元组
a = ()  # 定义一个空的元组
#2、定义 tuple()
print((tuple('123'),tuple('abc')))
print(tuple([1,2,3]))
#3、定义 用逗号直接隔开
a = 1,2,3,4
print(a)

# 增删改查方法 都没有
# 只有index() count()

# 函数返回多个变量 实际返回的是一个元组
def func():
    age = 20
    name = 'wf'
    return age, name
print(type(func()))

# 字符串
'''
字符串有序的 不可修改的 元素以 引号 包围的序列
'''
# 定义一个字符串
a = 'abc'
b = 'cccc'
c = """44444"""
d = '''222222'''
# 如果字符串中有单引号 那么要使用双引号来定义
# 反之 如果字符串中有双引号、那么要使用单引号来定义
e = "what's your name"
f = 'I say: "hello,kunpeng"'
# '''''' 三引号 可以定义带有换行符的多行字符串
j = """
i am kenpeng
i come from jiangsu
"""
# 字符串方法
# 格式化
# 1.%  %s字符串 %d 整型 %f浮点型  类型对应
s = 'hello %s %d元 已到账'
value = ('kunoneg', 300)
print(s % value)
# 2. {} format() 顺序对应
s = 'hello {} {}元 已到账'.format('kenpeng', 40)
print(s)
# 3. f
name = 'kunopeng'
money = 100
s = f"你好{name} 你充值的{money} 已到账"
s = f'你好{name} 你充值的{money} 已到账'
print(s)

# 字符串拼接
# 1.+ * 产生新的字符串
# 2.join 按照自定义的方式 连接列表中的元素（元素必须为字符类型）为字符串
l = ['a', 'b', 'c']
print(','.join(l))
#print(','.join([1,2,3]))  # 报错

# 字符串切分
# split() 制定切分对象 次数 默认以空格切分 返回一个列表
a = 'i am kupeng i am kupeng'
print(a.split(' ', 2)) #分割符 分割次数

# splitlines 行切分字符串
a = """
i am kupeng 
i am kupeng'
i am kupeng i am kupeng'
"""
print(a.splitlines())

# 字符串替换  replace
a = 'i am kupeng i am from jiangsu'
print(a.replace('i', 'I'))
print(a.replace('i', 'I', 2)) # 替换次数

# 字符串的查找
#1、index() count()  find() 查找的必须是字符型
# find 查找 返回从左边第一个指定字符的索引 找不到返回-1
a = 'i am kupeng i am from jiangsu'
b = '12345sretet0'
# print(a.count('i'))
# print(a.index('i'))
# print(b.find('e',1))
#print(b.index('t'))



#字符串的修饰










