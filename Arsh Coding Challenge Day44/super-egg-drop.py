class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (N + 1) for _ in range(K + 1)]
        
        for n in range(1, N + 1):
            dp[1][n] = n
        for k in range(2, K + 1):
            x = 1 
            for n in range(1, N + 1):
                while x < n and dp[k-1][x-1] < dp[k][n-x]:
                    x += 1
                dp[k][n] = 1 + dp[k-1][x-1]
        
        return dp[K][N]
