# Two pointer approach
# one points to num1, second one points to num2

# Plan:
# Initialize pointers
# Loop through both arrays at the same time
#   - compare element from num1 with num2 and swap if needed
# Edge cases: if length of num1 == length of num2 -> write num2 elements to num1


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1 = m - 1 # last element in num1
        p2 = n - 1 # last element in num2
        p = m + n - 1 # last position in num1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else: 
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # if nums2 has leftovers, place them
        # if nums1 has leftovers, they're already in place
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

        
        # NOT COrrect
        # l, r = 0, 0

        # if len(nums1) == len(nums2):
        #     nums1 = nums2

        # while l < m and r < n:
        #     if nums1[l] > nums2[r]:
        #         nums1[l], nums2[r] = nums2[r], nums1[l]
        #     l += 1
        #     r += 1

        # for i in range(m, m+n):
        #     nums1[i] = nums2[1]
        