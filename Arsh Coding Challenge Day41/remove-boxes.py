from functools import cache
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def dp(l, r, k):
            if l > r: return 0
            while l + 1 <= r and boxes[l] == boxes[l + 1]:
                l += 1
                k += 1
            ans = (k+1) * (k+1) + dp(l+1, r, 0)
            for m in range(l + 1, r + 1):
                if boxes[l] == boxes[m]:
                    ans = max(ans, dp(m, r, k+1) + dp(l+1, m-1, 0))
            return ans

        return dp(0, len(boxes) - 1, 0)