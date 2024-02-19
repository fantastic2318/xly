def strStr(haystack: str, needle: str) -> int:
    next = getNext(needle)
    j = -1
    for i in range(len(haystack)):
        while j > -1 and haystack[i] != needle[j+1]:
            j = next[j]
        if haystack[i] == needle[j+1]:
            j += 1
        if j == len(needle)-1:
            return i - j
    return -1


def getNext(needle):
    j = -1
    next = ["" for _ in range(len(needle))]
    next[0] = j
    for i in range(1, len(needle)):
        while j > -1 and needle[i] != needle[j+1]:
            j = next[j]
        if needle[i] == needle[j+1]:
            j += 1
        next[i] = j
    return next


# print(getNext("abcdefg"))
# print(getNext("aabaaf"))


#print(strStr("aabaabaafa", "aabaaf"))
print(strStr("aaabcdefg", "abcdefg"))