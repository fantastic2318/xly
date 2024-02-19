# 如何实现 "1,2,3" 变成 ['1','2','3'] ?
def test(str1):
    list1 = str1.split(',')
    return list1
print(test('1,2,3'))

# 将列列表[['a','b','c'],['d','e','f'],['g','h']]中的元素依次展开，得到 ⼀一个新的列列表 ['a','b','c','d','e','f','g','h']
def test1(list1):
    list2 = []
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            list2.append(list1[i][j])
    return list2
print(test1([['a','b','c'],['d','e','f'],['g','h']]))

# 假设今天的上课时间为5678秒，编程计算今天上课时间是多少时，多少分，多 少秒，以“xx时xx分xx秒”的形式表示出来。
def timeCount(s):

      h = s//3600
      m = s % 3600 // 60
      ss = s % 3600 % 60
      return h, m, ss
print('{}时{}分{}秒'.format(timeCount(5678)[0],timeCount(5678)[1],timeCount(5678)[2]))

# 输⼊入字符串串，将字符串串的开头和结尾变成'+'，产⽣生⼀一个新的字符串串
def trans(str1):
    str2 = str1.center(len(str1)+2, '+')
    return str2
print(trans("skdfhfkhsfk"))

# 猜数 给定⼀一个定值，⽐比如说 99
# 让⽤用户输⼊入数字，给⽤用户三次机会，如果三次之内猜对了了(输⼊入的值等于99)， 显示猜测正确
# 如果三次之内没有猜对，退出循环，显示'stupid' 要求，⽤用2种⽅方式实现

# 方法一：
def digitGame1(value):
    for i in range(0, 3):
        ch = input("请输入数字（仅有三次机会）：")
        if int(ch) == value:
            return '猜对啦'
            break
    else:
        return 'stupid'
print(digitGame1(99))

# 方法二：

def digitGame2(value):
    for i in range(3):
        try:
            ch = input("请输入数字（仅有三次机会）：")
            if int(ch) == value:
                return '猜对啦'
        except ValueError:
            pass
    else:
        return 'stupid'

print(digitGame2(99))

# 输⼊入某年某月某⽇，判断这⼀天是这一年的第几天? 这边简单考虑，不考虑 闰年的情况。
def daysCount(t):
    month = t[4:6]
    m = int(month) * 30
    days = t[6:8]
    d = int(days)
    return m+d


print(daysCount('20150505'))

# 输出 101~200 之间的所有素数 素数，就是 只能被 1 和 ⾃自⼰己整除的数，
# 判断素 数的⽅方法:⽤一个数分别去除2到这个数的平⽅方根，如果能被整除，则表明此数 不不是素数，反之是素数。

def just(a,b):
    list1 = []
    for i in range(a, b+1):
        tmp = int(pow(i, 0.5))
        while tmp >= 2:
            if i % tmp == 0:
                break
            tmp -= 1
        else:
             list1.append(i)
    return list1

print(just(101, 200))




