def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    for i in range(len(nums)):
        left = i+1
        right = len(nums) - 1
        if nums[i] > 0:
            return res
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        while left < right:
            if nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while right > left and nums[right] == nums[right - 1]:
                    right -= 1
                while right > left and nums[left] == nums[left + 1]:
                    left += 1
                right -= 1
                left += 1
    return res

#print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))