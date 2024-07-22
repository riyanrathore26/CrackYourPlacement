class Solution:
    def productExceptSelf(self, nums, n):
        result = [1] * n
        print(result)
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result