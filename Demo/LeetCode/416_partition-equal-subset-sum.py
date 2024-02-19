class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        if sum % 2 == 1:
            return False
        target = sum // 2
        dp = [0] * 10001
        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])
        return dp[target] == target

s = Solution()
print(s.canPartition([1,5,11,5]))