class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = (n+1)*[0]
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

s = Solution()
print(s.fib(10))