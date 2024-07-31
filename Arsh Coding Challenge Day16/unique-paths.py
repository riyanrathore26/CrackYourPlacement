# TLE code
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         matrix = [[0 for i in range(n)]for i in range(m)]
#         count = 0
#         def rec(matrix,i,j):
#             nonlocal count
#             if i >= m or j >= n:
#                 return
#             if i == m - 1 and j == n - 1:
#                 count += 1
#                 return
#             rec(matrix,i+1,j)
#             rec(matrix,i,j+1)
#         rec(matrix,0,0)
#         return count
from math import comb


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m+n-2,m-1)