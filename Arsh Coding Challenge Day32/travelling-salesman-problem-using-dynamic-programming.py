class Solution:
    def total_cost(self, cost):
        n = len(cost)
        memo = [[-1] * (1 << (n + 1)) for _ in range(n + 1)]

        def fun(i, mask):
            # base case: if only ith bit and 1st bit is set in our mask,
            # it implies we have visited all other nodes already
            if mask == ((1 << i) | 3):
                return cost[0][i-1]  # adjusting indices for Python (1-indexed to 0-indexed)

            # memoization check
            if memo[i][mask] != -1:
                return memo[i][mask]

            res = float('inf')  # initialize the result of this sub-problem
            for j in range(1, n + 1):
                if (mask & (1 << j)) != 0 and j != i and j != 1:
                    res = min(res, fun(j, mask & (~(1 << i))) + cost[j-1][i-1])
            
            memo[i][mask] = res  # storing the minimum value
            return res

        # Start TSP from the first node (index 1 in the original, index 0 in Python)
        result = min(fun(i, (1 << (n + 1)) - 1) + cost[i-1][0] for i in range(2, n + 1))
        return result