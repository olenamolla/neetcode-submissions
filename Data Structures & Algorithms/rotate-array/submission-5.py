class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # naive approach
        # save everything from the array up to k separately
        # then assign eveything from k until the end to the beginning of the array
        # then append whatever you saved before

        # n = len(nums)
        # k = k % n
        # split_idx = n - k
        # before_k = nums[:split_idx]
        # after_k = nums[split_idx:]
        # l, r = 0, 0

        # while l < len(after_k):
        #     nums[l] = after_k[l]
        #     l += 1

        # while r < len(before_k):
        #     nums[l] = before_k[r]
        #     l += 1
        #     r += 1

        # Optimized Solution
        # Reverse the the entire array from index 0 to n-1
        # Reverse the first k elements (from 0 to k - 1)
        # Reverse the remaining elements (from k to n-1)
        n = len(nums)
        k = k % n
        

        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]

                l, r = l + 1, r - 1

        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)