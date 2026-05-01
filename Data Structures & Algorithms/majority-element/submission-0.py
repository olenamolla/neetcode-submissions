class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for k, v in freq.items():
            if v >= len(nums) / 2:
                return k