import java.util.*;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i = 0; // i is always behind or at j;
        Set<Character> set = new HashSet<>();
        int prevLength;
        int biggest = 0;
        for (int j = 0; j < s.length(); j++) {
            prevLength = set.size();
            set.add(s.charAt(j));
            if (prevLength == set.size()) {
                biggest = Math.max(prevLength, biggest);
                i = delElems(set, i, j, s);
            }
        }
        return Math.max(set.size(), biggest);
        
        
    }
    public int delElems(Set<Character> set, int i, int j, String s) {

        while (s.charAt(i) != s.charAt(j)) {
            set.remove(s.charAt(i++));
        }

        return i+1;
    }
    public static void main(String[] args) {
        String s = "aabaab!bb";
        System.out.println(new Solution().lengthOfLongestSubstring(s));
    }
}