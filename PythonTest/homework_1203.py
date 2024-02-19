# 1.实现选择排序 难度等级 II
"""
算法描述:
1. 在⼀个长度为 N 的⽆无序数组中，第一次遍历 n-1 个数找到最⼩的和第⼀一个数交换。
2. 第二次从下一个数开始遍历 n-2 个数，找到最⼩小的数和第二个数交换。
3. 重复以上操作直到第 n-1 次遍历最小的数和第 n-1 个数交换，排序完成。
"""

def selectSort(list1):
    for i in range(len(list1)):
        minIndex = i
        for j in range(len(list1)-1, minIndex-1, -1):
            if list1[j] < list1[minIndex]:
                minIndex = j
        list1[minIndex], list1[j] = list1[j], list1[minIndex]
    return list1

print(selectSort([20,23,1,43,12,9]))



#2.统计文件内 字符串个数 有文件 a.txt(内容不为空，且有多⾏) 要求: 找出现次数最多的字符
# https://blog.csdn.net/qq_41617060/article/details/130886077
def genReader():
    with open('a.txt', 'r', encoding='utf-8', newline='\n') as file:
        for line in file:
            yield line.strip().split(',')
dict1 = {}
count = 1
for r in genReader():
    for i in r:
        dict1[i] = dict1.get(i, 0) + 1
d = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
print(d[0][0])


# 3.实现算法，找出列表中第⼆大的数, 如列列表 [3,5,2,8,4,7,9] 第二大 的数是 8
import heapq
def secondNum(list1, n):
    maxSec = []
    for i in list1:
        heapq.heappush(maxSec, i)
        if len(maxSec) > n:
            heapq.heappop(maxSec)
    return maxSec[0]

print(secondNum([3,5,2,8,4,7,9],2))

def find_sec(list1):
    secMaxValue = maxValue = 0
    for i in list1:
        if i >= maxValue:
            secMaxValue = maxValue
            maxValue = i
        elif i >= secMaxValue and i <= maxValue:
            secMaxValue = i
    return secMaxValue
print(find_sec([3,5,2,8,4,7,9]))





#4.定义⼀一个函数，实现传⼊入整数的累乘的和，⽐比如传⼊入5 ，实现 1+2!+3!+...+5!的和。
def mulSum(n):
    sum1 = 1
    for i in range(2, n+1):
        s1 = 1
        for j in range(i, 0, -1):
            s1 *= j
        sum1 += s1
    return sum1
print(mulSum(5))
# 5*4*3*2*1  3*2*1  4*3*2*1 2*1 1


# 5.输⼊入⼀一个整数n，⽤⽣成器打印出从 0~n 中的所有偶数

def generatorFunc(n):
    for i in range(0, n+1, 2):
            yield i

gen = generatorFunc(5)
for g in gen:
    print(g)


