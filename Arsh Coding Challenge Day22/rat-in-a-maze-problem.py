from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        result = []
        n = len(m)
        directions = {'D': (1, 0), 'U': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
        
        def backTrack(i, j, s):
            if i == n - 1 and j == n - 1 and m[i][j] == 1:
                result.append(s)
                return True

            if i < 0 or i >= n or j < 0 or j >= n or m[i][j] == 0:
                return False
            
            m[i][j] = 0  # Mark as visited

            for d in directions:
                ni, nj = i + directions[d][0], j + directions[d][1]
                backTrack(ni, nj, s + d)
            
            m[i][j] = 1  # Unmark for other paths

        if m[0][0] == 1:
            backTrack(0, 0, "")
        
        return result
