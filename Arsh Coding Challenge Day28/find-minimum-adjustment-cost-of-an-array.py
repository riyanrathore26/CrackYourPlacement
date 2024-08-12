class Solution:
    def minAdjustmentCost(self, arr, n, target):
        # DP table
        dp = [[float('inf')] * 101 for _ in range(n)]
        
        # Initialize the first row of dp
        for i in range(101):
            dp[0][i] = abs(arr[0] - i)
        
        # Fill the DP table
        for i in range(1, n):
            for j in range(101):
                for k in range(max(0, j - target), min(100, j + target) + 1):
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + abs(arr[i] - j))
        
        # The answer is the minimum value in the last row of dp
        return min(dp[-1])
