class Solution {
    public int removeElement(int[] nums, int val) {
        // edge cases
        // 1. Empty array
        // 2. All elements in the array == val
        // 3. No val at all - return size of the array

        // Implementation
        // 1. Initialize a pointer k = 0 to track the position for the next valid element
        int k = 0;
        // 2. Iterate through the array with index i
        for(int i = 0; i < nums.length; i++){
            //  2a. If nums[i] != val, copy it to nums[k] and increment k
            if(nums[i] != val){
                nums[k] = nums[i];
                k++;
            }

        }
        
        // 3. Return k as the count of valid elements
        return k;
    }
}