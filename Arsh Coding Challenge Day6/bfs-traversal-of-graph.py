#User function Template for python3

from typing import List
from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        visited = set()
        que = deque([0])  # Assuming the BFS starts from node 0
        result = []

        while que:
            node = que.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        que.append(neighbor)

        return result