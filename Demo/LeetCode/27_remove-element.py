def removeElement(nums,val):
    j = 0
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j


print(removeElement([3, 2, 2, 3], 3))