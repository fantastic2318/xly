def dinarySearch(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = left + int((right-left)/2)
        if target < nums[mid]:
            right = mid -1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    return -1
print(dinarySearch([-1,0,3,5,9,12],9))


