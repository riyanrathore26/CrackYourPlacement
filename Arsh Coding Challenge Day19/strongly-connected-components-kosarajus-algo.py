class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        def dfs(node):
            visited[node] = True
            for nbr in adj[node]:
                if not visited[nbr]:
                    dfs(nbr)
            stack.append(node)

        def dfs2(node, component):
            visited[node] = True
            component.append(node)
            for nbr in transposed[node]:
                if not visited[nbr]:
                    dfs2(nbr, component)
        
        stack = []
        visited = [False for _ in range(V)]
        for i in range(V):
            if not visited[i]:
                dfs(i)
        
        transposed = [[] for _ in range(V)]
        for i in range(V):
            for nbr in adj[i]:
                transposed[nbr].append(i)
        
        scc = []
        visited = [False] * V
        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                dfs2(v, component)
                scc.append(component)
        return len(scc)
