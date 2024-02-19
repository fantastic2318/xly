def groupAnagrams(strs: list[str]) -> list[list[str]]:
    hashmap = dict()
    for s in strs:
        key = ''.join(sorted(s))
        print(sorted(s))
    #     if key in hashmap:
    #         hashmap[key].append(s)
    #     else:
    #         hashmap[key] = [s]
    # return list(hashmap.values())



print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))