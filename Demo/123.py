# def triangles():
#     L = [1]  # 定义L为一个只包含一个元素的列表
#     while True:
#         yield L  # 定义为生成器函数
#         L = [1] + [L[n] + L[n - 1] for n in range(1, len(L))] + [1]
#
#
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break


# def fib(max):
#     n, a, b = 0,0,1
#     while n < max:
#         yield b # 设置B为生成器
#         a,b = b, a+b
#         n = n+1
# # 循环生成器、得到每次的值
# for f in fib(6):
#     print(f)
#     f = f + 1
#     if f == 7:
#         break


def test(weight, bagWeight, value):
    dp = [[0]*bagWeight for _ in range(0, len(weight))]
    for j in range(weight[0], bagWeight+1):
        dp[0][j] = value[0]
    for i in range(len(weight)):
        for j in range(weight[0], bagWeight+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])

    return dp[-1][-1]


print(test([1, 3, 4], 4, [15, 20, 30]))