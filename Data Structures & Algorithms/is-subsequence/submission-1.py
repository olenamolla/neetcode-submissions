class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:


        if len(s) > len(t):
            return False

        if s is None:
            return True

        tt = sorted(t)
        ss = sorted(s)

        i = j = 0
        while i < len(s) and j < len(t):
            if ss[i] == tt[j]:
                i += 1
            j += 1
        
        return i == len(s)
