class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        
        // Brute force - nested loops
        // for(int i = 0; i < nums.length; i++){
        //     for(int j = i+1; j < nums.length; j++){
        //         if(nums[i] + nums[j] == target){
        //             return new int[]{i, j};
        //         }
        //     }
        // }

        // Optimized:
        // HashMap
        // Instantiating a hashmap
        Map<Integer, Integer> seen = new HashMap<>();

        // filling it out with array elements
        // key = array element, value = element's index
        for(int i = 0; i < nums.length; i++){
            seen.put(nums[i], i);
        }

        // looping through the array
        // finding the complement from the target
        // if that complement number in the map, return its index together with array's element's index
        for(int i = 0; i < nums.length; i++){
            int complement = target - nums[i];

            if(seen.containsKey(complement) && seen.get(complement)!= i){
                return new int[]{i,seen.get(complement)};
            }
        }

    return new int[]{};
    }
}
