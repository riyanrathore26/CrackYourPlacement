from collections import defaultdict
from typing import List

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
        
        start = None
        for key, neighbors in graph.items():
            if len(neighbors) == 1:
                start = key
                break
        
        result = [start]
        while len(result) < len(adjacentPairs) + 1:
            last = result[-1]
            for neighbor in graph[last]:
                if len(result) == 1 or neighbor != result[-2]:
                    result.append(neighbor)
                    break
        
        return result