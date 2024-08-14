class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(node, parent, discovery_time):
            visited[node] = True
            low[node] = ids[node] = discovery_time
            discovery_time += 1
            
            for nbr in graph[node]:
                if nbr == parent:
                    continue
                if not visited[nbr]:
                    dfs(nbr, node, discovery_time)
                    low[node] = min(low[node], low[nbr])
                    if low[nbr] > ids[node]:
                        critical_edges.append([node, nbr])
                else:
                    low[node] = min(low[node], ids[nbr])

        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ids = [0] * n
        low = [0] * n
        critical_edges = []

        dfs(0, -1, 0)
        
        return critical_edges
