class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()){
            return false;
        }

        // Efficient solution is with frequency array

        int[] freq = new int[26]; // one clot per each letter

        for (char c : s.toCharArray()){
            freq[c - 'a']++;
        }

        for (char c: t.toCharArray()){
            freq[c - 'a']--;
        }

        for(int count : freq){
            if (count != 0){
                return false;
            }
        }
        return true;

        // char[] sortedS = s.toCharArray();
        // char[] sortedT = t.toCharArray();

        // Arrays.sort(sortedS);
        // Arrays.sort(sortedT);

        // return new String(sortedS).equals(new String(sortedT));
    }
}
