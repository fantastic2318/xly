class Solution:
    """
    动态规划
    """
    # dp含义：每一个nums[i]和前一个nums[i-1]相加后 和现在相比的最大值
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        print(dp)
        return max(dp)

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))