from collections import deque

class Solution:
    def shortestBridge(self, grid):
        # 1 for land
        # 2 for visited
        # 0 for water
        n = len(grid)
        def dfs(x, y):
            grid[x][y] = 2
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                    dfs(nx, ny)
        def bfs():
            while queue:
                x, y, dist = queue.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            return dist
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 2
                            queue.append((nx, ny, dist + 1))
        queue = deque()
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))        
        return bfs()