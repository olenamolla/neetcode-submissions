class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            # startswith() check the whole prefix at once
            # while loop does repeating chopping
            #  we chop until the current string starts with the prefix
            while not strs[i].startswith(prefix): 
                prefix = prefix[:-1]

                if not prefix:
                    return ""
        return prefix

        # Time = O(n * m) length * number
        # Space = O(1)
        