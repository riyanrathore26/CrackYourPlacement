class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            
            max_length = 1
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    max_length = max(max_length, 1 + dfs(x, y))
            
            dp[i][j] = max_length
            return dp[i][j]
        
        m, n = len(matrix), len(matrix[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        result = 0
        
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        
        return result
