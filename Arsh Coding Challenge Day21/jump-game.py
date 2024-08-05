# from typing import List

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         def dfs(ind):
#             if ind >= len(nums) - 1:
#                 return True
#             if nums[ind] == 0:
#                 return False
#             for i in range(1, nums[ind] + 1):
#                 if dfs(ind + i):
#                     return True
#             return False
#         return dfs(0)
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for i, jump in enumerate(nums):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + jump)
        return True