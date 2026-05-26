class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()){
            return false;
        }

        char[] sortedS = s.toCharArray();
        char[] sortedT = t.toCharArray();

        Arrays.sort(sortedS);
        Arrays.sort(sortedT);

        String sSort = new String(sortedS);
        String tSort = new String(sortedT);

        if (sSort.equals(tSort)){
            return true;
        } else {
            return false;
        }
    }
}
