class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        left, right = 0, 1

        while right < len(nums):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
                # left += 1
            else:
                right += 1

        return left + 1