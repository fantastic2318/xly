class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, int(i/2)+1):
                dp[i] = max(max(j*(i-j), j*dp[i-j]), dp[i])
        return dp[n]

s = Solution()
print(s.integerBreak(10))
