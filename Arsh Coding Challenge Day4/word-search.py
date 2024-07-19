# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         def dfs(mat,i,j):
#             if i > len(mat) && j > len(mat[0]):
#                 return 
#             dfs(mat,i+1,j)
#             dfs(mat,i,j+1)
#             dfs(mat,i-1,j)
#             dfs(mat,i,j-1)
#         i,j = 0,0
#         while i < len(board):
#             while j < len(board[0]):
#                 if board[i][j] == word[0]:
#                     dfs(board,i,j)
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, word, i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            temp = board[i][j]
            board[i][j] = '#'  # Mark the cell as visited
            found = (dfs(board, word, i + 1, j, k + 1) or
                     dfs(board, word, i - 1, j, k + 1) or
                     dfs(board, word, i, j + 1, k + 1) or
                     dfs(board, word, i, j - 1, k + 1))
            board[i][j] = temp  # Unmark the cell
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(board, word, i, j, 0):
                    return True
        return False
