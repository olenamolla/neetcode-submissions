class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        result = 1

        for i in range(len(nums)):
            curr_max = nums[i]
            curr_min = nums[i]

            for j in range(i + 1, len(nums)):
                curr_max = max(curr_max, nums[j])
                curr_min = min(curr_min, nums[j])

                if curr_max - curr_min <= limit:
                    result = max(result, j - i + 1)
                else:
                    break

        return result
        