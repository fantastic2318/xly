def minSubArrayLen(target: int, nums: list[int]) -> int:
    sum = 0
    j = 0
    res = float("inf")  # 无限大 float("-inf")无限小
    for i in range(len(nums)):
        sum += nums[i]
        while sum >= target:
            res = min(res, i-j+1)
            sum -= nums[j]
            j += 1
    if res == float("inf"):
        return 0
    else:
        return res


print(minSubArrayLen(7, [2,3,1,2,4,3]))
print(minSubArrayLen(4, [1,4,4]))
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))