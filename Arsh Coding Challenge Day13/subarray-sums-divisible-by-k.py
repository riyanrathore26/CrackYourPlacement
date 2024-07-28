from ast import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        hashmap = {0: 1}
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in hashmap:
                count += hashmap[prefix_sum - k]
            if prefix_sum in hashmap:
                hashmap[prefix_sum] += 1
            else:
                hashmap[prefix_sum] = 1
        return count 