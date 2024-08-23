from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)

        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0
            if dst in graph[src]:
                return graph[src][dst]
            
            visited.add(src)
            for neighbor, val in graph[src].items():
                if neighbor not in visited:
                    product = dfs(neighbor, dst, visited)
                    if product != -1.0:
                        return val * product
            visited.remove(src)
            return -1.0
        
        results = []
        for q1, q2 in queries:
            results.append(dfs(q1, q2, set()))
        
        return results