class Solution {
    public int[] getConcatenation(int[] nums) {
        
        int[] concat = new int[2 * nums.length];

        for(int i = 0; i < nums.length; i++){
            concat[i] = nums[i];
            concat[i + nums.length] = nums[i];
        }
        
        return concat;

    }
    
}

// Looping once - O(n) - time

// Space is O(n) too, because we created a new array