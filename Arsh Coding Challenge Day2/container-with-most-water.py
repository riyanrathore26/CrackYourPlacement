from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        h=len(height)-1
        mx = 0
        while l<h:
            mx = max(mx,min(height[l],height[h])*(h-l))
            if height[l]<height[h]:
                l+=1
            else:
                h-=1
        return mx