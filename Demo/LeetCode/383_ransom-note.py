def canConstruct(ransomNote: str, magazine: str) -> bool:
    hashmap = {}
    for s in ransomNote:
        if s in hashmap:
            hashmap[s] += 1
        else:
            hashmap[s] = 1
    for i in magazine:
        if hashmap.get(i):
            hashmap[i] -= 1
    for v in hashmap.values():
        if v != 0:
            return False
    return True

print(canConstruct("fihjjjjei" ,"hjibagacbhadfaefdjaeaebgi"))
