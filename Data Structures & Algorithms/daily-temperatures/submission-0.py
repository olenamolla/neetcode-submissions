class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack - stack holds indices of days still waiting for a warmer day
        # the temperature at those are in decreasing order
        # when a new temp is warmer that the stack's top, we pop and reslve - that day just found its answer

        # Plan:
        # 1. Create a res array that stores indices. The stack will maintain a monotonically descresaing order of temps
        # 2. Iterate through each day (index i)
        # 3. while the stack is not empty and the curr temp is greater than the temp at the index on top of the stack - 
        #    pop the top index, and set result[popped_index] = i - popped_index
        # 4. Push the curr index onto the stack
        # 5. After the loop, anything left on the stack never found a warmer day - they stay 0
        # Edge cases: single element - result 0
        #             all decreasing - nothing ever gets popped
        #             all the same temps - all 0s
        # Time and Space - O(n) because each index is pushed and popped at most once
        #                - O(n) for the stack and res array

        n = len(temperatures)

        result = [0] * n 
        stack = []

        for i in range(n): # iterating through each day
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index # distance in days

            stack.append(i)

        return result