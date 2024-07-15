from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        k = 0
        for i in range(1, n):
            if nums[i] > nums[k]:
                k += 1
                nums[k] = nums[i]
        return k + 1