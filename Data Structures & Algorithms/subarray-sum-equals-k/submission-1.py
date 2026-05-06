class Solution:
    # if all elements in the array = k, then output is the length of the array
    # if element is k, +1 subbaray
    # once sum of elements equals k, +1 subarray


    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # prefixSums = { sum : how_many_times_we_saw_it }
        res, curSum = 0, 0
        prefixSums = {0: 1} # represents the starting point before the array begins.

        for num in nums:
            # Add current element to running total
            curSum += num
            # What sum do I need to have seen earlier, 
            # so that the chunk between there and HERE sums to k
            diff = curSum - k
            # how many earlier points had that odometer reading?
            # if diff exists in HashMap → return its count
            # if diff doesn't exist → return 0

            res += prefixSums.get(diff, 0)
            # After checking, we record our current odometer reading into the HashMap.
            # we record AFTER checking, never before. If we recorded first, we'd count 
            # the current position as a valid earlier position, which is wrong
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res

        
        
        # numSubarr = 0

        # for i in range(len(nums)):
        #     # You need to accumulate the sum as j moves forward:
        #     current_sum = 0
        #     for j in range(i, len(nums)):
        #         current_sum += nums[j]
        #         if current_sum == k:
        #             numSubarr += 1

        # return numSubarr