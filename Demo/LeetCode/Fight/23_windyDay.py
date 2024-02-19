# 字符串 包含数字 特殊字符 数字相邻 1，,2，,3  ax1234,;''1234;1;
def test(s):
    tmp1 = []
    sum_1 = 0

    for i in range(len(s)):
        tmp = s[i]
        while s[i] >= 86 and s[i] <= 96 :
            tmp1.append(s[i])
            i+=1
            tmpSum = sumSum(tmp1)
        sum_1 += tmpSum



def sumSum(l):
    sum1= 0
    for i in l:
        sum1+=int(i)
    return sum1