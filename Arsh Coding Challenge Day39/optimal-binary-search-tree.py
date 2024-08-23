class Solution:
    
    def cost(self, arr, i, j):
        
        count = 0
        
        while i <= j:
            count += arr[i]
            i += 1
        return count
    
    def helper(self, i, j, freq, mem):
        
        # base case
        if i > j:
            return 0
            
        # check if the ans is pre-computed
        key = str(i) + ":" + str(j)
        
        if key in mem:
            return mem[key]
            
        cost = self.cost(freq, i, j)
        
        ans = float("inf")
        
        for k in range(i, j + 1):
            
            temp_ans = cost + self.helper(i, k - 1, freq, mem) + self.helper(k + 1, j, freq, mem)
            
            ans = min(ans, temp_ans)
            
        mem[key] = ans
        return ans
        
    def optimalSearchTree(self, keys, freq, n):
        
        mem = {}
        return self.helper(0, n - 1, freq, mem)