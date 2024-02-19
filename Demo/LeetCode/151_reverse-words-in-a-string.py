def removeSpace(s):
    left = 0
    right = len(s)-1
    while left <= right and s[left] == " ":
        left += 1
    while left <= right and s[right] == " ":
        right -= 1
    temp = []
    while left <= right:
        if s[left] != " ":
            temp.append(s[left])
        elif temp[-1] != " ":
            temp.append(s[left])
        left += 1
    return temp


def reverseStr(s):
    left = 0
    right = len(s) - 1
    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


def reverseEachWord(s):
    index1 = 0
    index2 = 0
    while index1 < len(s):
        if s[index1] != " ":
            index1 += 1
        else:
            s[index2: index1] = reverseStr(s[index2: index1])
            index1 += 1
            index2 = index1
        if index1 == len(s)-1:
            s[index2: index1+1] = reverseStr(s[index2: index1+1])

    return s


def reverseWords(s: str) -> str:
    s = list(s)
    s = removeSpace(s)
    #return "".join(s)
    rStr = reverseStr(s)
    #return rStr
    rEW = reverseEachWord(rStr)
    return "".join(rEW)


print(reverseWords(" the sky  is   blue   "))
#print(reverseEachWord(['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']))

