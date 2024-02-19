class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        c = self.reverse1(nums)
        a = self.reverse1(c[0:k])
        b = self.reverse1(c[k: len(c)])
        return a + b

    """
            Do not return anything, modify nums in-place instead.
           """
    def rotate2(self,  nums: list[int], k: int):
        k = k % len(nums)
        nums = self.reverse1(nums)
        nums[0:k] = self.reverse1(nums[0:k])
        nums[k:len(nums)] = self.reverse1(nums[k: len(nums)])


    def reverse1(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums



s = Solution()
print(s.rotate(nums = [1,2,3,4,5,6,7], k = 3))

