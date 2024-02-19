# 使用二维数组解决0-1背包问题
def bagValue2(weight, bagWeight, value):
    # 初始化dp数组 dp[i][j]数组表示在【0，i】范围内取任意物品i放到重量是j的背包内的最大价值
    dp = [[0]*(bagWeight+1) for _ in range(0, len(weight))]
    # 初始化dp[0][j] 就是只放物品0无论背包的重量是多少(前提是背包容量要大于物品0的重量（weight[0]）)，对应的价值都是value[0]
    #return dp
    for j in range(weight[0], bagWeight+1):
        dp[0][j] = value[0]
    #return dp
    for i in range(1, len(weight)):  # 先遍历物品 正序
        for j in range(0, bagWeight+1):  # 再遍历背包 正序
            if j < weight[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
    return dp[-1][-1]


print(bagValue2([1, 3, 4], 4, [15, 20, 30]))

def test(weight, bagWeight, value):
    dp = [[0]*(bagWeight+1) for _ in range(0, len(weight))]
    for j in range(weight[0], bagWeight+1):
        dp[0][j] = value[0]
    for i in range(1, len(weight)):
        for j in range(weight[0], bagWeight+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])

    return dp[-1][-1]


print(test([1, 3, 4], 4, [15, 20, 30]))


# 使用一维数组解决0-1背包问题
def bagValue1(weight, bagWeight, value):
    # 初始化dp[j]数组 表示背包容量为j的最大价值为dp[j]、相当于是把二维数组压缩了为了一维数组、重复利用覆盖一维数组的值
    dp = [0 for _ in range(bagWeight+1)]
    for i in range(0, len(weight)): # 先遍历物品 正序
        for j in range(bagWeight, weight[i]-1, -1): # 再遍历背包 倒序 背包容量的最小值应该要大于物品的重量 否则无法装
            dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
    return dp[-1]


print(bagValue1([1, 3, 4], 4, [15, 20, 30]))