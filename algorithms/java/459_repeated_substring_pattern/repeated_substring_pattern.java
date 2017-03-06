import java.util.Scanner;

/**
 * @author Peng
 * 
 * Problem:
 *      Given a non-empty string check if it can be constructed 
 *      by taking a substring of it and appending multiple copies of the substring together.
 *      You may assume the given string consists of lowercase English letters only 
 *      and its length will not exceed 10000.
 *      
 *      Example 1:
 *          Input: "abab"
 *          Output: True
 *          Explanation: It's the substring "ab" twice.
 */
public class repeated_substring_pattern {

    /**
     * Solution 1: using brute-force
     * 
     * Idea: 
     *      the length of substring must can be divided by the length of whole string;
     *      so, we can repeated all possibles substring to check.
     * 
     * @param s
     * @return true if repeating substring is existed.
     */
    public static boolean repeatedSubstringPattern_1(String s) {
        int len = s.length();
        
        for(int i = len/2; i >= 1; i--) {
            if(len%i == 0) {  // one possible substring length
                int sub_len = len/i;
                String sub_s = s.substring(0, i);
                int j;
                for(j = 1; j < sub_len; j++) {
                    if(!sub_s.equals(s.substring(j * i, i + j * i)))  break;
                }
                if(j == sub_len)  return true;  
            }
        }
        return false;
    }
    
    /**
     * Solution 2: using a little trick
     * 
     * Idea: 
     *      for a repeated string s with length N:
     *      set that repeating substring sub_s with length M;
     *      st. first char: s[0] = sub_s[0]
     *          last char:  s[N-1] = sub_s[M-1]
     *      we set s2 = s + s
     *         and remove s2[0] and s2[2N-1]
     *         st. if s appears once in s2, 
     *         the first index s appears in s2 is M,
     *         which means s is repeated by sub_s 
     *              
     * @param s
     * @return true if repeating substring is existed.
     */
    public static boolean repeatedSubstringPattern_2(String s) {
        String s2 = s + s;
        s2 = s2.substring(1, 2 * s.length() - 1);
        if(s2.contains(s)) return true;
        return false;
    }
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("please input a string:");
        while(scan.hasNext()){
            String str = scan.nextLine();
            System.out.println(repeatedSubstringPattern_1(str));
            System.out.println(repeatedSubstringPattern_2(str));
        }
        scan.close();
    }

}
