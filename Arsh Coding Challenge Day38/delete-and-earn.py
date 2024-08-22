from collections import Counter
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        hashTable = Counter(nums)

        for val, count in hashTable.items():
            hashTable[val] = val * count
        
        max_num = max(nums)
        dp = [0] * (max_num + 1)
        
        dp[1] = hashTable.get(1, 0)
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i-1], dp[i-2] + hashTable.get(i, 0))
        
        return dp[max_num]
