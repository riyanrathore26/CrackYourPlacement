class Solution:
    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        visited = [False for _ in range(V)]
        stack = []
        
        def dfs(node, visited, stack, adj):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor, visited, stack, adj)
            stack.append(node)
        
        for i in range(V):
            if not visited[i]:
                dfs(i, visited, stack, adj)
        return stack[::-1]