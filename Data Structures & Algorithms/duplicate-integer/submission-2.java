class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> unique = new HashSet<>();

        for(int num: nums){
            unique.add(num);
        }

        if(unique.size() == nums.length){
            return false;
        } else {
            return true;
        }

    }
}