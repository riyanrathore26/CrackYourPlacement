class Solution:
    def minInsertions(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]        
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1        
        return dp[0][n-1]