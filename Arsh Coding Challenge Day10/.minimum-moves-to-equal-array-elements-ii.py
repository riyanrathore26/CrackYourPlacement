class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        print(median)
        return sum(abs(num - median) for num in nums)
        # nums.sort()
        # result = []
        # for i in range(len(nums)):
        #     li = []
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         li.append(abs(nums[i]-nums[j]))
        #     result.append(li)
        # mx = float('inf')
        # for i in range(len(result)):
        #     mx = min(mx,sum(result[i]))
        # return mx