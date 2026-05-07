class Solution:
    # if all elements in the array = k, then output is the length of the array
    # if element is k, +1 subbaray
    # once sum of elements equals k, +1 subarray


    def subarraySum(self, nums: List[int], k: int) -> int:
        numSubarr = 0

        for i in range(len(nums)):
            # You need to accumulate the sum as j moves forward:
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    numSubarr += 1

        return numSubarr