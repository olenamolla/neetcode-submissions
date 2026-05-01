import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack = []
        # operators = {'+', '-', '*', '/'}
        # # 1. Iterate through each token in the array
        # for token in tokens:
        #     if token in operators:
        #         right = stack.pop()
        #         left = stack.pop()

        #         if token == '+':
        #             result = left + right
        #         elif token == '-':
        #             result = left - right
        #         elif token == '*':
        #             result = left * right
        #         else:
        #             result = int(left / right)

        #         stack.append(result)
        #     else:
        #         stack.append(int(token))
        # return stack[0]
        # 2. If the token is a number, convert it to integer, and push it onto the stack"
        # 3. If the token is an operator, pop the two top elements.
        #    The first pop is the right operand, the second pop is the left operand. Apply the operator and push the result back.
        # 4. After processing all tokens, the stack will have exactly one element - that is the answer
        # Edge cases: 
        # Division must truncate toward zero - I will use int(a/b) instead of a//b
        # Negative number tokens like -3 int() handles fine
        # Single token input - never hits an operator, just return that single token
        # Time and Space Complexity

        # More pythonic way



        stack = []
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)
        }

        for token in tokens:
            if token in ops:
                right = stack.pop()
                left = stack.pop()

                stack.append(ops[token](left, right))

            else:
                stack.append(int(token))

        return stack[0]