class Solution:
    def isKPartitionPossible(self, nums, k):
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        target = total_sum // k
        nums.sort(reverse=True) 
        used = [False] * len(nums)

        def backtrack(start, k, current_sum):
            if k == 1:
                return True  
            if current_sum == target:
                return backtrack(0, k - 1, 0) 
            for i in range(start, len(nums)):
                if not used[i] and current_sum + nums[i] <= target:
                    used[i] = True
                    if backtrack(i + 1, k, current_sum + nums[i]):
                        return True
                    used[i] = False
            
            return False

        return backtrack(0, k, 0)
