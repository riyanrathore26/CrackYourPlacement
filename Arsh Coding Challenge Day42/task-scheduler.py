import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)
        
        time = 0
        
        while max_heap:
            temp_list = []
            for _ in range(n + 1):
                if max_heap:
                    temp_list.append(heapq.heappop(max_heap))

            for count in temp_list:
                if count + 1 < 0:
                    heapq.heappush(max_heap, count + 1)
            
            if max_heap:
                time += n + 1
            else:
                time += len(temp_list)

        return time
