from typing import List
class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(start):
            if start > n:
                return 1
            count = 0
            for i in range(start, n + 1):
                if nums[i] % start == 0 or start % nums[i] == 0:
                    nums[start], nums[i] = nums[i], nums[start]
                    count += backtrack(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]
            return count
        
        nums = list(range(n + 1))
        return backtrack(1)