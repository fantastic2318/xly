def fourSum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    res = []
    for i in range(len(nums)):
        if nums[i] > target and (nums[i] >=0 or target >= 0):
            return res
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for k in range(i+1, len(nums)):
            if k > i+1 and nums[k] == nums[k-1]:
                continue
            left = k + 1
            right = len(nums)-1
            while left < right:
                if nums[i] + nums[k] + nums[left] + nums[right] < target:
                    left += 1
                elif nums[i] + nums[k] + nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res.append([nums[i], nums[k], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
    return res

print(fourSum([1,0,-1,0,-2,2],0))