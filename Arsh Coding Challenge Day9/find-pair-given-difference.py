from typing import List

class Solution:
    def findPair(self, n: int, x: int, arr: List[int]) -> int:
        arr.sort()
        i, j = 0, 1  # Start with two pointers

        while i < n and j < n:
            if i != j:
                temp = abs(arr[j] - arr[i])
                if temp == x:
                    return 1
                elif temp < x:
                    j += 1
                else:
                    i += 1
            else:
                j += 1

        return -1
     