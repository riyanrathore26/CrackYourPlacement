from collections import deque
from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        dq = deque()
        max_value = float('-inf')
        
        for x, y in points:
            while dq and x - dq[0][1] > k:
                dq.popleft()            
            if dq:
                max_value = max(max_value, y + x + dq[0][0])
                
            while dq and y - x >= dq[-1][0]:
                dq.pop()
            
            dq.append((y - x, x))
        
        return max_value
