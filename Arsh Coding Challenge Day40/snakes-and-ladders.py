from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        # Flatten the board into a 1D list to simplify the traversal
        def get_board_value(index):
            r, c = divmod(index - 1, N)
            if r % 2 == 0:
                return board[N - 1 - r][c]
            else:
                return board[N - 1 - r][N - 1 - c]
        
        queue = deque([(1, 0)]) 
        visited = [False] * (N * N + 1)
        visited[1] = True
        
        while queue:
            current_square, rolls = queue.popleft()
            
            if current_square == N * N:
                return rolls
            
            # Roll the dice for 1 to 6
            for dice in range(1, 7):
                next_square = current_square + dice
                if next_square <= N * N:
                    board_value = get_board_value(next_square)
                    if board_value != -1:
                        next_square = board_value
                    if not visited[next_square]:
                        visited[next_square] = True
                        queue.append((next_square, rolls + 1))
        
        return -1 