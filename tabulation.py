#=====================Tabulation
def minCostClimbingStairs(cost):
    n = len(cost)
    if n == 0:
       return 0
    if n == 1:
       return cost[0]

    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

    return min(dp[n - 1], dp[n - 2])
cost = [10, 15, 20]
print(minCostClimbingStairs(cost))