class Solution:
    def isCycle(self, V, adj):
        visited = [0 for _ in range(V)]  # 0 = unvisited, 1 = visiting, 2 = visited
        
        def dfs(node,parent):
            visited[node] = 1  # mark as visiting
            for neighbor in adj[node]:
                if visited[neighbor] == 0:  # if unvisited
                    if dfs(neighbor,node):
                        return True
                elif neighbor != parent:  # if visiting
                    return True
            visited[node] = 2  # mark as visited
            return False
        
        for i in range(V):
            if visited[i] == 0:
                if dfs(i,-1):
                    return True
        return False