from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(ind, lists):
            result.append(lists[:])
            for i in range(ind, len(nums)):
                lists.append(nums[i])
                backtrack(i + 1, lists)
                lists.pop()
        result = []
        backtrack(0, [])
        return result