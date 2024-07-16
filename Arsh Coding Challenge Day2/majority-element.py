from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums)//2
        for i in set(nums):
            if nums.count(i) > maj:
                return i