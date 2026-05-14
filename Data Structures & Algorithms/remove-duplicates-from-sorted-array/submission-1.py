class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 1

        # left, right = 0, 1

        # while right < len(nums):
        #     if nums[right] != nums[left]:
        #         left += 1
        #         nums[left] = nums[right]
        #         # left += 1
        #     else:
        #         right += 1

        # return left + 1

        # Plan:
        # have two pinters - left and right, left starts at 0, right at 1
        # traverse through the array using while loop
        # if next element is not equal to the previous one - ove rigth onw forward

        if len(nums) == 1:
            return 1

        l, r = 0, 1

        while r < len(nums):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
            else:
                r += 1
        
        return l + 1



