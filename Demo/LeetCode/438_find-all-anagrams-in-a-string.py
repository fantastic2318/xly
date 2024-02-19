def findAnagrams(s: str, p: str) -> list[int]:
    j = 0
    index = []
    for i in range(len(p)-1, len(s)):
        if isAnagram(s, p, j, i):
            index.append(j)
            j += 1
        else:
            j += 1
    return index


def isAnagram(s, p, x, y):
    hashmap = dict()
    for i in s[x:y+1]:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    for j in p:
        if j in hashmap:
            hashmap[j] -= 1
        else:
            hashmap[j] = 1
    for v in hashmap.values():
        if v != 0:
            return False
    return True


#print(findAnagrams("cbaebabacd", "abc"))
print(findAnagrams("abab", "ab"))