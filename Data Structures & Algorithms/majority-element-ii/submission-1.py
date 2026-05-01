class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # build a freq table for nums
        # initiate the result array
        # loop through the dict, add to the result array elements that appear more than n/3

        # Not the optimal solution but solved myself
        # freq = {}
        # result = []
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1

        # for k, v in freq.items():
        #     if v > len(nums) / 3:
        #         result.append(k)

        # return result

        # Boyer Moore Voting Algorithm
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        
        result = []

        for c in [candidate1, candidate2]:
            if c is not None and nums.count(c) > len(nums) / 3:
                result.append(c)

        return result

