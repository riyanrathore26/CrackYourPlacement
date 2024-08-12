from collections import defaultdict
from typing import List

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        answer = [0] * n
        count = [1] * n
        
        def dfs1(node, parent):
            for neighbor in tree[node]:
                if neighbor != parent:
                    dfs1(neighbor, node)
                    count[node] += count[neighbor]
                    answer[node] += answer[neighbor] + count[neighbor]
        
        def dfs2(node, parent):
            for neighbor in tree[node]:
                if neighbor != parent:
                    answer[neighbor] = answer[node] + (n - count[neighbor]) - count[neighbor]
                    dfs2(neighbor, node)
        
        dfs1(0, -1)
        dfs2(0, -1)
        return answer
