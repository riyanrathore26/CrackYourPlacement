from collections import deque

class Solution:
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        directions = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        # Convert to 0-indexed positions
        start = (KnightPos[0] - 1, KnightPos[1] - 1)
        end = (TargetPos[0] - 1, TargetPos[1] - 1)

        # Queue for BFS
        queue = deque([(start, 0)])  # (position, steps)
        visited = set()
        visited.add(start)

        while queue:
            (x, y), steps = queue.popleft()
            
            if (x, y) == end:
                return steps

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), steps + 1))

        return -1
