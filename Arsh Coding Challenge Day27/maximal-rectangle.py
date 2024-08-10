from typing import List


class Solution:
    def dfs(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        max_area = 0
        
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        heights.pop()
        return max_area
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0 for _ in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    dp[i][j] = dp[i-1][j] + int(matrix[i][j])
        mx = 0
        for i in range(row):
            mx = max(mx,self.dfs(dp[i]))
        return mx