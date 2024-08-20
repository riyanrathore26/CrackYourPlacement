from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0), (1,1), (1,-1), (0,1), (0,-1), (-1,0), (-1,1), (-1,-1)]
        
        def countLiveNeighbors(i, j):
            live = 0
            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and abs(board[ni][nj]) == 1:
                    live += 1
            return live
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                live_neighbors = countLiveNeighbors(i, j)
                
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1  # Mark as live to dead
                else:
                    if live_neighbors == 3:
                        board[i][j] = 2
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0
