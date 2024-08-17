from typing import List


class Solution:
    def uniquePathsIII(self, matrix: List[List[int]]) -> int:
        count = 0
        n = len(matrix)
        m = len(matrix[0])
        empty_count = 0 
        start_x = start_y = end_x = end_y = -1
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    empty_count += 1
                elif matrix[i][j] == 1:
                    start_x, start_y = i, j
                elif matrix[i][j] == 2:
                    end_x, end_y = i, j

        def rec(matrix, i, j, remain):
            nonlocal count
            if i < 0 or i >= n or j < 0 or j >= m or matrix[i][j] == -1:
                return
            if i == end_x and j == end_y:
                if remain == 0:
                    count += 1
                return

            # Mark as visited
            temp = matrix[i][j]
            matrix[i][j] = -1
            
            # Recur for 4 directions
            rec(matrix, i+1, j, remain-1)
            rec(matrix, i-1, j, remain-1)
            rec(matrix, i, j+1, remain-1)
            rec(matrix, i, j-1, remain-1)

            matrix[i][j] = temp

        rec(matrix, start_x, start_y, empty_count+1)
        return count
