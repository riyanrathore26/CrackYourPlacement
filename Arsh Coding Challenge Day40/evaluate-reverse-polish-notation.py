from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i)) 
            elif i in "+-*/":
                val2 = stack.pop() 
                val1 = stack.pop() 
                if i == '+':
                    stack.append(val1 + val2)
                elif i == '-':
                    stack.append(val1 - val2)
                elif i == '*':
                    stack.append(val1 * val2)
                elif i == '/':
                    stack.append(int(val1 / val2))
        return stack.pop()
