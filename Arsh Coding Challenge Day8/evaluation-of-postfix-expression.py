def evaluatePostfix(exp):
    stack = []

    # Iterate over each character in the expression
    for char in exp:
        if char.isdigit():
            # Push the operand (character) as an integer
            stack.append(int(char))
        else:
            # Pop the two topmost operands
            val1 = stack.pop()
            val2 = stack.pop()

            # Perform the operation and push the result back onto the stack
            if char == '+':
                stack.append(val2 + val1)
            elif char == '-':
                stack.append(val2 - val1)
            elif char == '*':
                stack.append(val2 * val1)
            elif char == '/':
                stack.append(int(val2 / val1))  # Ensure integer division

    # The result will be the only element left in the stack
    return stack.pop()

# Example usage:
postfix_exp = "231*+9-"
print(f"Evaluation of postfix expression {postfix_exp}: {evaluatePostfix(postfix_exp)}")
