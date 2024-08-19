class Solution:
    def largestIsland(self,grid):
        n = len(grid)
    
        def dfs(x, y, island_id):
            if not (0 <= x < n and 0 <= y < n and grid[x][y] == 1):
                return 0
            grid[x][y] = island_id  # Mark the cell with the island ID
            return 1 + dfs(x+1, y, island_id) + dfs(x-1, y, island_id) + dfs(x, y+1, island_id) + dfs(x, y-1, island_id)
    
        island_id = 2
        island_sizes = {0: 0}
    
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[island_id] = dfs(i, j, island_id)
                    island_id += 1
        max_island = max(island_sizes.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen_islands = set()
                    current_size = 1 
                    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if 0 <= x < n and 0 <= y < n and grid[x][y] > 1:
                            island_id = grid[x][y]
                            if island_id not in seen_islands:
                                seen_islands.add(island_id)
                                current_size += island_sizes[island_id]
                
                    max_island = max(max_island, current_size)
    
        return max_island