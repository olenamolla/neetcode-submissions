class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()){
            return false;
        }

        char[] sortedS = s.toCharArray();
        char[] sortedT = t.toCharArray();

        Arrays.sort(sortedS);
        Arrays.sort(sortedT);

        return new String(sortedS).equals(new String(sortedT));
    }
}
