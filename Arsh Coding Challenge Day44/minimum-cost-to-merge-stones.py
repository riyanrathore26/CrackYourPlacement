import sys
from typing import List

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]
        
        dp = [[0] * n for _ in range(n)]
        
        for length in range(k, n + 1):  # length of the range
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = sys.maxsize

                # Try splitting the subarray into two parts
                for mid in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j])
                # If we can merge the whole subarray into one pile, add the cost
                if (length - 1) % (k - 1) == 0:
                    dp[i][j] += prefix_sum[j + 1] - prefix_sum[i]
                    print(dp)
        return dp[0][n - 1]
