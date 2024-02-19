

def test(weight, bagWeight, value):
    dp = [[0]*bagWeight for _ in range(0, len(weight))]
    for j in range(weight[0], bagWeight+1):
        dp[0][j] = value[0]
    for i in range(len(weight)):
        for j in range(weight[0], bagWeight+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])

    return dp[-1][-1]


print(test([1, 3, 4], 4, [15, 20, 30]))