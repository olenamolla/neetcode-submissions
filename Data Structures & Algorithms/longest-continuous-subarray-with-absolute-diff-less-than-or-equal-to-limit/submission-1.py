class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_d = deque()
        min_d = deque()

        result = 0
        left = 0
        for right in range(len(nums)):

            while max_d and nums[max_d[-1]] <= nums[right]:
                max_d.pop() # bigger number arrived
            max_d.append(right) # storing indices

            while min_d and nums[min_d[-1]] >= nums[right]:
                min_d.pop()
            min_d.append(right)

            while nums[max_d[0]] - nums[min_d[0]] > limit:
                left += 1 # shrinking the window from the left
                if max_d[0] < left:
                    max_d.popleft() # max element is outside of the window, remove it

                if min_d[0] < left:
                    min_d.popleft()
            
            result = max(result, right - left + 1)
        
        return result