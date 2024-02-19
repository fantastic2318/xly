# def test(file):
#     with open(file, "r", encoding="utf-8") as fe:
#         fe.read()





#"时间戳:2022-11-18 16:26,ip:127.0.0.1, api1: vv/ss, time:10ms massage: "


# 1,5,2,4,-1,9,7,6,3,10

def findElem(nums):
    hashmap = {}
    for i, v in enumerate(nums):
        hashmap[v] = i

    # 排序
    nums.sort()
    left = 1
    right = len(nums)-1
    # 找缺失的位置 和 应该放置的位置
    while left <= right:
        mid = left + int((right - left)/2)
        if mid != nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if left == len(nums) -1 and nums[left] == left:
        for i in hashmap.keys():
            if i < 0:
                return [left+1, hashmap[i]]
    else:
        return [left, len(nums)]

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        for i, x in enumerate(nums):
            if i != x:
                return i
        return n


print(findElem([1,5,2,4,-1,9,7,6,3,10]))


#'{"params":{"id":222,"offset":0},{"nodename":"topic"}'
#"时间戳:2022-11-18 16:26,ip:127.0.0.1, api1: vv/ss, time:10ms massage: "