#------------------------Climingstairs using cost Recursion----------------

def minCostClimbingStairs(cost):
    memo = {}
    def minCost(i):
        if i >= len(cost):
            return 0
        if i in memo:
            return memo[i]
        memo[i] = cost[i] + min(minCost(i + 1), minCost(i + 2))
        return memo[i]
    return min(minCost(0), minCost(1))

cost = [10, 15, 20]
print(minCostClimbingStairs(cost))

#-------------------------n to 0

def minCostClimbingStairs(cost):
    memo = {}
    n = len(cost)
    def minCost(i):
        if i == 0:
            return cost[0]
        if i == 1:
            return cost[1]
        if i in memo:
            return memo[i]
        memo[i] = cost[i] + min(minCost(i - 1), minCost(i - 2))
        return memo[i]
    return min(minCost(n - 1), minCost(n - 2))
cost = [10, 15, 20]
print(minCostClimbingStairs(cost))