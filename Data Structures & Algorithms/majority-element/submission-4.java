class Solution {
    public int majorityElement(int[] nums) {
        // using hashmap approach
        // create the hashmap
        // num's element is key, its count is value
        Map<Integer, Integer> counts = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            counts.put(nums[i], counts.getOrDefault(nums[i], 0) + 1);
            
            if(counts.get(nums[i]) > nums.length / 2){
                return nums[i];
            }
        }
        throw new IllegalStateException("No majority element");

        // loop over the array and fill out the hashmap
    }
}