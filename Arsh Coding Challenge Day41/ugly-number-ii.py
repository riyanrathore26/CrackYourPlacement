class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        p1 = p2 = p3 = 0
        
        for i in range(1, n):
            twomul = dp[p1] * 2
            threemul = dp[p2] * 3
            fivemul = dp[p3] * 5
            
            dp[i] = min(twomul, threemul, fivemul)
            
            if dp[i] == twomul:    
                p1 += 1
            if dp[i] == threemul:    
                p2 += 1
            if dp[i] == fivemul:    
                p3 += 1
        
        return dp[-1]