from collections import deque

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        n_rows = len(grid)
        n_cols = len(grid[0])

        def bfs(i, j):
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                if 0 <= x < n_rows and 0 <= y < n_cols and grid[x][y] == 1:
                    grid[x][y] = 0  # Mark the cell as visited
                    directions = [
                        (1, 0), (-1, 0), (0, 1), (0, -1),
                        (1, 1), (1, -1), (-1, 1), (-1, -1)
                    ]
                    for dx, dy in directions:
                        queue.append((x + dx, y + dy))

        count = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 1:
                    count += 1
                    bfs(i, j)

        return count
