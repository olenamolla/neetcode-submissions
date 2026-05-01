class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # water stored is the area of the container
        # width is (right index - left)
        # height is the max of the actual array elements

        # need to use two pointer approach
        # traverse over the array, check start and end elements 
        # with each other

        # brute force

        # max_area = 0

        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         max_area = max(max_area, min(heights[i], heights[j]) * (j-i))

        # return max_area

        # Two pointer approach
        # gives us O(n) time 

        l = 0
        r = len(heights) - 1

        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)

            res = max(res, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
