from collections import deque

class Solution:
    def orangesRotting(self, grid):
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time_elapsed = 0

        while queue:
            r, c, time = queue.popleft()
            time_elapsed = max(time_elapsed, time)

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                    grid[new_r][new_c] = 2
                    fresh_oranges -= 1
                    queue.append((new_r, new_c, time + 1))

        return -1 if fresh_oranges > 0 else time_elapsed
