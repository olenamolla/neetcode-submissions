class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        right_boundary = [n] * n
        stack = []

        for i in range(n):
            # current stack is shorter than top of the stack
            # current bar is the right boundary fot top
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                right_boundary[index] = i
            stack.append(i)


        left_boundary = [-1] * n
        stack = []

        for i in range(n-1, -1, -1):
            #current bar is shorter than topnof the stack
            # current bar is the left boundary for top
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                left_boundary[index] = i
            stack.append(i)

        max_area = 0
        for i in range(n):
            width = right_boundary[i] - left_boundary[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)
        return max_area
