def repeatedSubstringPattern(s: str) -> bool:
    a = len(s)
    next = getNext(s, a)
    if next[-1] != -1 and a % (a - (next[-1] + 1)) == 0:
        return True
    else:
        return False


def getNext(s, a):
    j = -1
    next = [0 for _ in range(a)]
    next[0] = j
    for i in range(1, a):
        while j > -1 and s[i] != s[j+1]:
            j = next[j]
        if s[i] == s[j+1]:
            j += 1
        next[i] = j
    return next


print(repeatedSubstringPattern("abcabcabcabc"))
print(repeatedSubstringPattern("aba"))
print(repeatedSubstringPattern("abab"))
