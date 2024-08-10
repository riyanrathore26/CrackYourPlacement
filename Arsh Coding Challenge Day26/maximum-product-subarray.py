# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [0] * n
#         dp[0] = nums[0]
#         for i in range(1,n):
#             dp[i] = max(nums[i],nums[i]*nums[i-1])
#         return max(dp)
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        max_prod = min_prod = result = nums[0]

        for i in range(1, n):
            current_max = max_prod
            
            max_prod = max(nums[i], nums[i] * max_prod, nums[i] * min_prod)
            min_prod = min(nums[i], nums[i] * current_max, nums[i] * min_prod)
            
            result = max(result, max_prod)

        return result
