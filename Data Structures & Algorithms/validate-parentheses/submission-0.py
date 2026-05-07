# valid strings - "((({[]})))"
# the most recently opened bracket must be closed first
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        brackets = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        if len(s) == 0:
            return True

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif ch in ")]}" and brackets[ch] == stack[-1]:
                if stack:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
                