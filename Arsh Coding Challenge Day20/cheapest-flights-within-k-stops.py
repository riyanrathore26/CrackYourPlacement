import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        for u, v, w in flights:
            adj[u].append((v, w))
        pq = [(0, src, k + 1)]       
        visited = {}
        while pq:
            cost, node, stops = heapq.heappop(pq)
            if node == dst:
                return cost
            if stops > 0:
                for neighbor, price in adj[node]:
                    new_cost = cost + price
                    if (neighbor, stops - 1) not in visited or new_cost < visited[(neighbor, stops - 1)]:
                        visited[(neighbor, stops - 1)] = new_cost
                        heapq.heappush(pq, (new_cost, neighbor, stops - 1))
        return -1
