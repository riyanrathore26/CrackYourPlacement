class Solution:
    def isCyclic(self, V, adj):
        visited = [0 for _ in range(V)]  # 0 = unvisited, 1 = visiting, 2 = visited
        
        def dfs(node):
            visited[node] = 1
            for neighbor in adj[node]:
                if visited[neighbor] == 0:  # if unvisited
                    if dfs(neighbor):
                        return True
                elif visited[neighbor] == 1:  # if visiting
                    return True
            visited[node] = 2 
            return False
        
        for i in range(V):
            if visited[i] == 0:
                if dfs(i):
                    return True
        return False