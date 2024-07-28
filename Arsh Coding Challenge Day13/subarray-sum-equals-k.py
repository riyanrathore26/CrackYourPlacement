from ast import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] + nums[i+1] == k:
                count +=1
            elif nums[i] == k:
                count+=1
        return count