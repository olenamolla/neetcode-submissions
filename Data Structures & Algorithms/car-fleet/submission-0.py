class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Pair each car's position and speed together, then sort by position in descending order (closest to the target first)
        # 2. For each car, calculate its time to reach the target: time = (target - position) / speed
        # 3. Use a stack. For each car's time:
        # - if the stack is empty OR the current ime is greater than the top of the stack -
        #   this car forms a new fleet, push its time
        # - if the current time is less than or equal to the top -
        #   this car gets absorbed into the fleet ahead, do not push
        # 4. Return the length of the stack - that's the number of fleet
        # Edge cases: 
        # -  single car -> one fleet
        # -  all cars same speed -> that's number of fleets

        # Complexity: O(n log n) time for the sort, O(n) space for the stack and paired array

        cars = sorted(zip(position, speed), reverse=True)

        stack = [] # to store time-to-target for each fleet

        for pos, speed in cars:
            time = (target - pos) / speed

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)