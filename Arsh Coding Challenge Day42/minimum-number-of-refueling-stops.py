import heapq
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_reach = startFuel
        count, index = 0, 0
        max_heap = []
        
        while max_reach < target:
            # Add all reachable stations to the max-heap
            while index < len(stations) and stations[index][0] <= max_reach:
                heapq.heappush(max_heap, -stations[index][1])
                index += 1
            
            if not max_heap:
                return -1
            
            # Refuel with the largest fuel available
            max_reach += -heapq.heappop(max_heap)
            count += 1
        
        return count
