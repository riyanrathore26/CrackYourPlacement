from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        n_rows = len(grid)
        n_cols = len(grid[0])

        def backTrack(i, j):
            if i < 0 or i >= n_rows or j < 0 or j >= n_cols or grid[i][j] == '0':
                return

            grid[i][j] = '0'  
            backTrack(i + 1, j)
            backTrack(i - 1, j)
            backTrack(i, j + 1)
            backTrack(i, j - 1)

        count = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == '1':
                    count += 1
                    backTrack(i, j)

        return count