def removeDuplicates(nums):
    j = 0
    for i in range(0, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    return j+1


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))