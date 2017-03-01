import java.util.Scanner;

public class power_of_two {
    
    /**************************************************
     * Solution1:
     *  Method:
     *      considering of bit operation;
     *      2's power numbers are:  1, 2, 4, 8, 16 ...
     *                      binary: 1, 10, 100, 1000, 10000 ...
     *      observe that: the number have 1bit of 1 at top digit.
     *                    the rest is 0.
     *      so, we can count the bit of 1;
     **************************************************/
    public static class Solution1 {
        public boolean isPowerOfTwo(int n) {
            if(n < 0) return false;
            if(Integer.bitCount(n) == 1) return true;
            else return false;
        }
    }
    
    /**************************************************
     * Solution2:
     *  Method:
     *      extending of solution1;
     *      consider: a number is power of 2, whose binary is 100000...
     *                st. number-1 's binary is 011111...
     *                st. number & (number - 1) = 0; 
     **************************************************/
    public static class Solution2 {
        public boolean isPowerOfTwo(int n) {
            return (n > 0) && ( (n & (n-1)) == 0 );
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();
        
        Solution1 s1 = new Solution1();
        Solution2 s2 = new Solution2();
        System.out.print( s1.isPowerOfTwo(n) );
        System.out.print( s2.isPowerOfTwo(n) );
    }

}
