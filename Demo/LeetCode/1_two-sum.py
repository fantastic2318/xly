def twoSum(nums, target):
    hashmap = {}
    for index, value in enumerate(nums):
        if target-value in hashmap:
            return [index, hashmap[target-value]]
        hashmap[value] = index


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 3], 6))