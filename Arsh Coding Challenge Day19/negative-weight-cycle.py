class Solution:
	def isNegativeWeightCycle(self, n, edges):
        dist = [float('inf')] * n
        dist[0] = 0  # Let's start from vertex 0 (arbitrary choice)
        
        # Relax all edges |V| - 1 times.
        for _ in range(n - 1):
            for u, v, weight in edges:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
        
        # Check for negative-weight cycles.
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                return 1  # If we can still relax an edge, then we have a negative cycle
        
        return 0
