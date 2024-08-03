from collections import defaultdict
class Solution:
    def isPossible(self, N, P, prerequisites):
        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            
            visited[node] = 1 
            for nbr in graph[node]:
                if not dfs(nbr):
                    return False
            visited[node] = 2 
            return True

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        visited = [0] * N
        for i in range(N):
            if visited[i] == 0:
                if not dfs(i):
                    return False
        return True