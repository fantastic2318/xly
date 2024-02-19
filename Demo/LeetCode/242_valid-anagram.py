def isAnagram(s, t):
    if len(s) != len(t):
        return False
    hashmap = dict()
    for i in s:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    for j in t:
        if j in hashmap:
            hashmap[j] -= 1
        else:
            hashmap[j] = 1
    for v in hashmap.values():
        if v != 0:
            return False
    return True


print(isAnagram("rat","car"))
print(isAnagram("anagram","nagaram"))
print(isAnagram("anagra","nagaram"))