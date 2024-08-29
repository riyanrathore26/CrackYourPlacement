from heapq import heappop, heappush
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        min_heap = [(grid[0][0], 0, 0)]  # (elevation, x, y)
        visited[0][0] = True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        maxi = grid[0][0]

        while min_heap:
            elevation, x, y = heappop(min_heap)
            maxi = max(maxi, elevation)
            if x == n - 1 and y == n - 1:
                return maxi
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heappush(min_heap, (grid[nx][ny], nx, ny))

        return -1