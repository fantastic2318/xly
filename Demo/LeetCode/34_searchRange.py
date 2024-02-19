def searchRange(nums, target):
    if len(nums) == 0:
        return [-1, -1]
    index = dinarySearch(nums, target)
    left = index
    right = index
    if index != -1:
        while left >= 0 and nums[left] == target:
            left -= 1
        while right <= len(nums)-1 and nums[right] == target:
            right += 1
        return [left+1, right-1]
    else:
        return [-1, -1]


def dinarySearch(nums, target):
    left = 0
    right = len(nums)
    while left <= right:
        mid = left + int((right-left)/2)
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    return -1


print(searchRange([5,7,7,8,8,10], 8))
print(searchRange([5,7,7,8,8,10], 6))
print(searchRange([], 0))