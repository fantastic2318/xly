# m = 3
# n = 4
# n = [[0 for i in range(n)] for j in range(m)]
# print(n)
#
# for i in range(0, 3):
#     print(i)
# '''
# 反向循环
# '''
# for i in range(3, 0, -1):
#     print(i)


#print(-17//8)
# print(int(9/5))
# print(4)
#
# print(3.0//2.0)
# print(6/3)

import collections


def minWindow(s: str, t: str) -> str:
    need = collections.defaultdict(int)
    for c in t:
        need[c] += 1
    needCnt = len(t)
    i = 0
    res = (0, float('inf'))
    for j in range(len(s)):
        if need[s[j]] > 0:
            needCnt -= 1
        need[s[j]] -= 1
        if needCnt == 0: # 说明都包含了
            while True:
                if need[s[i]] == 0:
                    break
                need[s[i]] += 1
                i += 1
            # 记录结果
            if j - i < res[1] - res[0]:
                res = (i, j)
            # 移动i 开始缩小窗口范围
            need[s[i]] += 1
            needCnt += 1
            i += 1
    if res == (0, float('inf')):
        return 0
    else:
        return s[res[0]:res[1]+1]


print(minWindow("ADOBECODEBANC", "ABC"))

