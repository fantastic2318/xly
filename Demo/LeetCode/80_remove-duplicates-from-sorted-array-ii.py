def removeDuplicates(nums: list[int]) -> int:
    # 写指针
    j = 0
    K = 2
    for i in range(len(nums)):
        if j < K or nums[i] != nums[j - K]:
            nums[j] = nums[i]
            j += 1
    return j


print(removeDuplicates([0,0,1,1,1,1,2,2,3,4]))