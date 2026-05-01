class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Time - O(n)
        # Space - O(n)
        # clearing the string - should contain only alphanumeric characters
        # filtered_chars = [ch.lower() for ch in s if ch.isalnum()]
        # # converting to string
        # clean_string = "".join(filtered_chars)
        # # initializing pointers for two pointer approach
        # l, r = 0, len(clean_string) - 1
        # # iterating over the string: one from the beginning, another one from the end
        # while l < r:
        #     if clean_string[l] != clean_string[r]:
        #         return False

        #     l += 1
        #     r -= 1

        # return True

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            # do not forget incrementing pointers
            l += 1
            r -= 1

        return True
