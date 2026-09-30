class Solution {
    public boolean hasDuplicate(int[] nums) {
        // create an empty hashset
        Set<Integer> seen = new HashSet<>();
        // loop through each number
        for (int num: nums){
            if (!seen.add(num)){
                return true;
            }
        }
        return false;
        // if the number is in the set, , return true
        // if not, add to the set
        // after the loop, return false

        // time - O(n)
        // space - O(n)

    }
}