import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = []
        for i in range(len(wage)):
            # Create pairs of (wage/quality ratio, quality)
            workers.append((wage[i] / quality[i], quality[i]))

        workers.sort(key=lambda p: p[0])

        max_heap = []
        total_quality = 0
        min_cost = float('inf')

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality += q

            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)

            if len(max_heap) == k:
                min_cost = min(min_cost, total_quality * ratio)

        return min_cost
