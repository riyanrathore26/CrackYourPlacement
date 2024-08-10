class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        moves = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],         # 5 can't move anywhere
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
        }
        dp = [[0] * 10 for _ in range(n)]
        for i in range(10):
            dp[0][i] = 1
        for k in range(1, n):
            for digit in range(10):
                dp[k][digit] = sum(dp[k-1][prev] for prev in moves[digit]) % MOD
        return sum(dp[n-1]) % MOD