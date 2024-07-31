from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result.append(matrix[i][j])
        result.sort()
        return result[k-1]