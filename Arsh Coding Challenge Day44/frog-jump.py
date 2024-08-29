from typing import List
from collections import defaultdict

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones or stones[0] != 0 or stones[1] != 1:
            return False
        
        dp = defaultdict(set)
        dp[0].add(0)
        
        for i in range(len(stones)):
            current_stone = stones[i]
            for jump in dp[current_stone]:
                for next_jump in [jump-1, jump, jump+1]:
                    if next_jump > 0 and current_stone + next_jump in stones:
                        dp[current_stone + next_jump].add(next_jump)
        
        return bool(dp[stones[-1]])
