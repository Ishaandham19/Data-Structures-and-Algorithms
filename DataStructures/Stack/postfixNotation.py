from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = {'+', '-', '*', '/'}
        for token in tokens:
            if token in operators:
                op_2 = int(stack.pop())
                op_1 = int(stack.pop())
                result = 0
                if token == '+':
                    result = op_1 + op_2
                elif token == '-':
                    result = op_1 - op_2
                elif token == '*':
                    result = op_1 * op_2
                elif token == '/':
                    result = int(op_1 / op_2)  # '//' operator floors to negative inf. Need int(op_1 / op_2) to truncate towards 0.
                else:
                    raise Expection("Invalid Operator")
                stack.append(str(result))
            else:
                stack.append(token)
        
        if len(stack) > 1:
            raise Expection("Invalid Expression")
            
        return int(stack[0])