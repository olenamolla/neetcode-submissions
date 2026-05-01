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
            elif stack and ch in ")]}":  
                if brackets[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False
                