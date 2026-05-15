class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 1. Sorting the array in ascending order
        # 2. Using two pointers: 0, and n - 1
        # 3. Initialize a boat counter
        # 4. While left is less than or equal to right:
        #   - calculate the remaining capacity after placing the heaviest person at right
        #   - decrement the right
        #   - if the lightest person at left fits the remaining capacity and left is still valid, increment left
        # 5. Return the boat count

        people.sort()
        l, r = 0, len(people) - 1
        boat_counter = 0

        while l <= r:
            remaining_capacity = limit - people[r]
            r -= 1

            boat_counter += 1

            if l <= r and remaining_capacity >= people[l]:
                l += 1
        return boat_counter

            