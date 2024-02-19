def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    new = []
    hashmap = dict()
    for i in nums1:
        if i not in hashmap:
            hashmap[i] = 1
    for i in nums2:
        if hashmap.get(i):
            new.append(i)
            hashmap[i] -= 1
    return new


print(intersection([1,2,2,1],[2,2]))
print(intersection([4,9,5],[9,4,9,8,4]))


