#请写一个 Python 函数，接受一个字符串，返回该字符串中每个字符出现的次数。

def test(str1):
    if len(str1) == 0:
        return None
    str2 = list(str1)
    hashmap = {}
    for i in str2:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    return hashmap

