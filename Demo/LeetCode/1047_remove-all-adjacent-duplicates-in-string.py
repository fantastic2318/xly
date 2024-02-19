# def removeDuplicates(s: str) -> str:
#     stack = []
#     for i in range(len(s)):
#         if len(stack) > 0 and stack[-1] == s[i]:
#             stack.pop()
#         else:
#             stack.append(s[i])
#     return stack


# 方法二，使用双指针模拟栈，如果不让用栈可以作为备选方法。

def removeDuplicates(s: str) -> str:
    res = list(s)
    slow = fast = 0
    length = len(res)

    while fast < length:
        # 如果一样直接换，不一样会把后面的填在slow的位置
        res[slow] = res[fast]

        # 如果发现和前一个一样，就退一格指针
        if slow > 0 and res[slow] == res[slow - 1]:
            slow -= 1
        else:
            slow += 1
        fast += 1

    return ''.join(res[0: slow])

print(removeDuplicates("abbaca"))