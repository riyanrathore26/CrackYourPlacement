from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        def backtrack(ind, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()
        
        result = []
        backtrack(0, [], 0)
        return result
