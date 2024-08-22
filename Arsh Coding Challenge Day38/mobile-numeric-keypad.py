#User function Template for python3
class Solution:
	def getCount(self, N):
        if N <= 0: # type: ignore
            return 0
        if N == 1:
            return 10

    # The keypad array
        keypad = [
        [0, 8],          # 0
        [1, 2, 4],       # 1
        [2, 1, 3, 5],    # 2
        [3, 2, 6],       # 3
        [4, 1, 5, 7],    # 4
        [5, 2, 4, 6, 8], # 5
        [6, 3, 5, 9],    # 6
        [7, 4, 8],       # 7
        [8, 5, 7, 9, 0], # 8
        [9, 6, 8],       # 9
        ]

        dp = [[0] * 10 for _ in range(N+1)] # type: ignore
    
    # Initialize DP table for length 1
        for i in range(10): # type: ignore
            dp[1][i] = 1

        for i in range(2, N+1):
            for j in range(10):
                dp[i][j] = 0
                for move in keypad[j]:
                    dp[i][j] += dp[i-1][move]
    
    # Sum up all the counts of length N
        total_count = 0
        for i in range(10): # type: ignore 
            total_count += dp[N][i]

        return total_count
