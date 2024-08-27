from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        inf = float('inf')
        dist = [[inf] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
        
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Step 4: Determine the city with the smallest number of reachable cities
        minReachable = n
        resultCity = -1
        
        for i in range(n):
            reachableCities = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            
            if reachableCities < minReachable or (reachableCities == minReachable and i > resultCity):
                minReachable = reachableCities
                resultCity = i
        
        return resultCity
