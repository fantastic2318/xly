def reverseStr(s, k):
    s = list(s)
    for i in range(0, len(s), 2*k):
        s[i:i+k] = reverse2k(s[i:i+k])

    return "".join(s)


def reverse2k(s):
    left = 0
    right = len(s)-1
    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


print(reverseStr("abcdefg",2))

