class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # optimized two pointer solution
        # helper function used not to use slicing
        # O(1) space
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return (is_palindrome(l+1, r) or
                        is_palindrome(l, r - 1))
            l += 1
            r -= 1
        return True










        # # time is O(n) - passing through the whole string
        # # space is O(n) - slicing and reversal creates new objects in memory
        # l, r = 0, len(s) - 1

        # while l < r:
        #     if s[l] != s[r]:
        #         skipL = s[l+1: r+1]
        #         skipR = s[l:r]

        #         # check if subarrays are palindromes agter skipping right and left character
        #         return skipL == skipL[::-1] or skipR == skipR[::-1]

        #     l += 1
        #     r -= 1

        # return True        