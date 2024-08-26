class Solution:
    def celebrity(self, mat):
        def knows(a, b):
            return mat[a][b] == 1
        
        n = len(mat)
        stack = []
        
        # Step 1: Push all persons to the stack
        for i in range(n):
            stack.append(i)
        
        # Step 2: Determine the potential celebrity
        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()
            
            if knows(a, b):
                stack.append(b)
            else:
                stack.append(a)
        
        # The potential celebrity
        candidate = stack.pop()
        
        # Step 3: Validate the candidate
        for i in range(n):
            if i != candidate:
                if knows(candidate, i) or not knows(i, candidate):
                    return -1  # No celebrity found
        
        return candidate  # The candidate is the celebrity
