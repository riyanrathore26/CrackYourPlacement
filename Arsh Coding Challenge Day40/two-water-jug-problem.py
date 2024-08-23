from collections import deque

class Solution:
    def minSteps(self, m: int, n: int, d: int) -> int:
        
        if d > max(m, n):
            return -1
        
        # If d is divisible by the GCD of m and n, then solution is possible
        if d % self.gcd(m, n) != 0:
            return -1
        
        # Use BFS to explore all possible states
        queue = deque([(0, 0)])  # Starting with both jugs empty
        visited = set()
        visited.add((0, 0))
        
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                a, b = queue.popleft()
                
                # If we found the desired amount of water in either jug
                if a == d or b == d:
                    return steps
                
                # Possible states from the current state
                next_states = [
                    (m, b),
                    (a, n),
                    (0, b),
                    (a, 0),
                    (min(a + b, m), b - (min(a + b, m) - a))
                    (a - (min(a + b, n) - b), min(a + b, n))
                ]
                
                for state in next_states:
                    if state not in visited:
                        visited.add(state)
                        queue.append(state)
            
            steps += 1
        
        return -1
    
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

