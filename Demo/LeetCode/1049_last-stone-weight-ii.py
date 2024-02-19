class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        weightSum = 0
        for i in range(len(stones)):
            weightSum += stones[i]
        target = weightSum // 2
        dp = 1501 * [0]
        for i in range(len(stones)):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i] )
        return weightSum - dp[target] - dp[target]


s = Solution()
print(s.lastStoneWeightII([31,26,33,21,40]))
