# input : two strings
# output: a new string constructed by merging given strings in alternating order:
#         one ch from str1, one ch from str2

# Match: Two pointer approach: one pointer traverses the str1, second one traverses str2
# Plan:
# 1. Initialize a new string and two pointers
# 2. Iterate through both strings at the first time and populate the new string
# 3. If one string is shorter, add the remaining characters from the longer string to the new string

# Edge cases:
# empty strings : nope, not possible
# if one string is empty, return the second one and vice versa: no possible
# if both strings are the same length - just add them together

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = ""
        i = 0

        # wrong!: concatenating != merging
        # if len(word1) == len(word2):
        #     result += word1 + word2

        
        # for i in range(min(len(word1), len(word2))):
            # Wrong: never triggers!
            # if not word1:
            #     result += word2[i:]
            
            # if not word2:
            #     result += word1[i:]

        #     result += word1[i]
        #     result += word2[i]
           
        # i = min(len(word1), len(word2))
        # result += word1[i:]
        # result += word2[i:] #one is always empty

        # return result

        res = []
        l, r = 0, 0

        while l < len(word1) and r < len(word2):
            res.append(word1[l])
            res.append(word2[r])
            l += 1
            r += 1

        res.append(word1[l:])
        res.append(word2[r:])

        return "".join(res)


        