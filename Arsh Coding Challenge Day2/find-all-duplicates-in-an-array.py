from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        sets = set()
        result = []
        for i in nums:
            if i in sets:
                result.append(i)
            else:
                sets.add(i)
        return result