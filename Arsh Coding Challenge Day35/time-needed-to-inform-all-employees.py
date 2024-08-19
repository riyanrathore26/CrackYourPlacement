from collections import defaultdict
from typing import List
class Solution:
    def numOfMinutes(self,n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                tree[manager[i]].append(i)

        def dfs(emp_id):
            max_time = 0
            for sub in tree[emp_id]:
                max_time = max(max_time, dfs(sub))
            return max_time + informTime[emp_id]
    
        return dfs(headID)
