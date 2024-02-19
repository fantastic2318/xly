class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        for i, x in enumerate(nums):
            if i != x:
                return i
        return n