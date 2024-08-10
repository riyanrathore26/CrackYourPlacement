from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        try:
            for i in range(0,len(prices)):
                if prices[i]<prices[i+1]:
                    mx += prices[i+1]-prices[i]
        except:
            pass
        return mx