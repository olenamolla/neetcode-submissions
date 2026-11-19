class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // It asks for k elements with the highest frequencies
        // Initialize a Hashmap

        Map<Integer, Integer> freqs = new HashMap<>();

        for(int num: nums){
            freqs.put(num, freqs.getOrDefault(num,0) + 1);
        }
        
        List<Integer> numbers = new ArrayList<>(freqs.keySet());
        numbers.sort((a,b) -> freqs.get(b) - freqs.get(a));

        int[] result = new int[k];
        for(int i = 0; i < k; i++){
            result[i] = numbers.get(i);
        }

        return result;
    }
}
