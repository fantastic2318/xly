def firstMissingPositive(nums: list[int]) -> int:
    nums = list(filter(lambda x: x > 0, list(set(nums))))
    if len(nums) == 0:
        return 1
    nums.sort()
    for i in range(1, len(nums) + 1):
        if nums[i - 1] != i:
            return i
    return nums[len(nums) - 1] + 1


print(firstMissingPositive([1,2,0]))