class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # 1. Initialize an empty stack to store valid scores
        # 2. For each operation:
        #    - if it is +, add the sum of the top two elements to the stack
        #    - if it's D, add double the top element to the stack
        #    - if it is C, pop the element
        #    otherwise, it is a number, s push it into the stack
        # 3. Return the sum of all elements in the stack

        stack = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)