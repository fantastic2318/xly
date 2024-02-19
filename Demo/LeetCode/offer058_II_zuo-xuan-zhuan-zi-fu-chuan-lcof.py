def reverseLeftWords(s: str, n: int) -> str:
    s = list(s)
    s = reverseStr(s)
    index = len(s)-1
    while index >= 0:
        if n != 0:
            n -= 1
            index -= 1
        else:
            s[index+1: len(s)] = reverseStr(s[index+1: len(s)])
            break
    s[:index+1] = reverseStr(s[:index+1])
    return "".join(s)


def reverseStr(s):
    left, right = 0, len(s)-1
    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

print(reverseLeftWords("abcdefg",2))
