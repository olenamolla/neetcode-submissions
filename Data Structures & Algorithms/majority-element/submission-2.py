class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # freq = {}

        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1

        # for k, v in freq.items():
        #     if v >= len(nums) / 2:
        #         return k

        # OR
        # count = defaultdict(int)
        # res=maxCount = 0

        # for num in nums:
        #     count[num] += 1
        #     if maxCount < count[num]:
        #         res = num
        #         maxCount = count[num]
        # return res

        # sorted(nums)

        # return nums[len(nums) // 2]


        # res = nums[0]
        # count = 1


        # Boyre Moore Voting Algorithm
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if candidate == num else -1)

        return candidate
