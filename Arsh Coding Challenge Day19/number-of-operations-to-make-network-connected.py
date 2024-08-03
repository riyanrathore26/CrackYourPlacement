from typing import List
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            visited[node] = True
            for nbr in adj[node]:
                if not visited[nbr]:
                    dfs(nbr)

        visited = [False for _ in range(n)]
        components = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1

        return components - 1