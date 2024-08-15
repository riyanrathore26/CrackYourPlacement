class Solution:
    def equalPartition(self, N, arr):
        total_sum = sum(arr)
        if total_sum %2 != 0:
            return False
        target = total_sum //2
        dp = [False]*(target+1)
        dp[0] = True
        
        for num in arr:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
            print(dp)
        return dp[target]
arr = [1,5,11,5]
obj = Solution()
obj.equalPartition(len(arr),arr)