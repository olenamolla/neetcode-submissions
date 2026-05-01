class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. create a dict where anagrams are sorted
        # 2. check the dict and append to the res list

        # res = defaultdict(list)

        # for s in strs:
        #     sorted_s = ''.join(sorted(s))
        #     res[sorted_s].append(s)
        # return list(res.values())

        # # since it involves sorting, time complexity is O(n * k * log k)

        # BELLOW IS SOLUTION for O (n * m)

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())