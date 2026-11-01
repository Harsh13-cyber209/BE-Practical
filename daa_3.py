def knapsack(wt, val, W):
    n = len(wt)

    dp = [[0] * (W + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):

            if wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]],
                               dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

wt = [2, 3, 4, 5]
val = [3, 4, 5, 6]

W = 5

print("Maximum Profit:", knapsack(wt, val, W))
