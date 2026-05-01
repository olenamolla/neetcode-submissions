


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
       
    #    # initializing ans with same elements as nums
    #    ans = nums[:] # this does not copy, it points to the same list, when you append to nums, 
    #               # you are modifying nums also(NOT OK) (ans = nums)
    #               # but nums[:] - is a slice that says "give me all elements from start to end" → creates a brand new list with the same values:
       
    #    # iterate n times
    #    for i in range(len(nums)):
        
    #     # append the nums elements to the end of the ans arr
    #     ans.append(nums[i])

    #    return ans

       # or even simpler solution
       return nums + nums

    

 