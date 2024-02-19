

# 一个整型数组里除了两个数字只出现一次，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字，如[1,2,3,3,2,9]返回[1,9]
def count(nums):
    if len(nums) == 0:
        return []
    hashmap = {}
    res = []
    for i in range(len(nums)):
        if nums[i] not in hashmap:
            hashmap[nums[i]] = 1
        else:
            hashmap[nums[i]] += 1
    for k, v in hashmap.items():
        if v == 1:
            res.append(k)
    return res



print(count([1,2,3,3,2,9]))