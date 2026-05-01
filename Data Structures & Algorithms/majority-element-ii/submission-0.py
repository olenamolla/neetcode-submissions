class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # build a freq table for nums
        # initiate the result array
        # loop through the dict, add to the result array elements that appear more than n/3

        freq = {}
        result = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for k, v in freq.items():
            if v > len(nums) / 3:
                result.append(k)

        return result