from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        def combo(ind, stack):
            if stack not in result:
                result.append(stack[:])
            for i in range(ind, len(nums)):
                if i > ind and nums[i] == nums[i - 1]:
                    continue
                stack.append(nums[i])
                combo(i + 1, stack)
                stack.pop()
        combo(0, [])
        return result