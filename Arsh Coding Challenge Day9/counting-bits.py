from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        count = 0
        li = []
        for i in range(n+1):
            count = bin(i).count('1')
            li.append(count)
        return li