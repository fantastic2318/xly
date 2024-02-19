class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        dp = [0] * (len(cost)+1)
        if len(cost) == 0:
            return 0
        if len(cost) == 0:
            return 0
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[-1]

s = Solution()
print(s.minCostClimbingStairs([10,15,20]))