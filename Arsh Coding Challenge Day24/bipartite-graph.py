
from collections import deque

class Solution:
    def isBipartite(self, V, adj):
        color = [-1] * V
        
        def bfs(source):
            que = deque([source])
            color[source] = 0
            
            while que:
                node = que.popleft()
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        que.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
            return True

        for i in range(V):
            if color[i] == -1:
                if not bfs(i):
                    return False
        
        return True