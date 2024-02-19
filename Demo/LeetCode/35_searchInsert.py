def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + int((right - left) / 2)
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    return left


#     def testFunc(self):
#         try:
#             assert self.searchInsert([1, 3, 5, 6], 5) == 2
#             assert self.searchInsert([1, 3, 5, 6], 5) == 1
#         except AssertionError as e:
#             return e.with_traceback()
#
#
# s = Solution()
# print(s.testFunc())

print(searchInsert([1, 3, 5, 6], 7))

