class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # l,r = 0, len(nums) - 1
        # while l <= r:
        #     if nums[l] == val and nums[r] != val:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l += 1
        #         r -= 1
        #     elif nums[l] != val:
        #         l += 1
        #     else:
        #         r -= 1
        
        # return l

        i = 0
        n = len(nums)

        while i < n :
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        return n


        