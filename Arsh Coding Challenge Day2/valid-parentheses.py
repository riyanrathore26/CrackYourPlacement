class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openstack = {'(': ')', '{': '}', '[': ']'}
        
        for char in s:
            if char in openstack:
                stack.append(char)
            elif stack and openstack[stack[-1]] == char:
                stack.pop()
            else:
                return False

        return not stack