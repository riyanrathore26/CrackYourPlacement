from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent.setdefault(x, x)
            parent.setdefault(y, y)
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        for stone in stones:
            union(~stone[0], stone[1])

        return len(stones) - len({find(x) for x in parent})

