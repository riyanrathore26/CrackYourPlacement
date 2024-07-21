#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited = [False for _ in range(V)]
        result = []
        def dfs(source):
            visited[source] = True
            result.append(source)
            for i in adj[source]:
                if not visited[i]:
                    dfs(i)
        dfs(0)
        return result