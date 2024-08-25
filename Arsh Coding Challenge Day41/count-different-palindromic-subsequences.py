MOD = 10**9 + 7

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = (2 * dp[i + 1][j - 1]) % MOD
                    l, r = i + 1, j - 1
                    while l <= r and s[l] != s[i]:
                        l += 1
                    while l <= r and s[r] != s[j]:
                        r -= 1
                    if l > r:
                        dp[i][j] = (dp[i][j] + 2) % MOD
                    elif l == r:
                        dp[i][j] = (dp[i][j] + 1) % MOD
                    else:
                        dp[i][j] = (dp[i][j] - dp[l + 1][r - 1]) % MOD
                else:
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
        
        return dp[0][n - 1]
