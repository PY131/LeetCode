/**
 * @author Peng
 *
 * @Problem:
 *  Implement int sqrt(int x).
 *  Compute and return the square root of x.
 *  
 *  note: find an integer w -> w * w = x' which x' <= x and (w+1)*(w+1) > x
 */
public class sqrt_x {

    /**
     * Solution 1: 
     *      the list of integer w ~ [0, x] is an sorted array, 
     *      so we can search every w to find the candidate one,
     *      but for a faster way is using binary search in the candidate array.
     * @param x
     * @return w
     * @Complexity: O(logn) cause of bin-search
     */
    public static int mySqrt_1(int x) {
        int lo = 0, hi = x;
        
        while(lo <= hi) {
            int mi = (lo + hi) >> 1;
            if((long)mi*mi > x) hi = mi - 1;  // using long type to avoid overflow
            else lo = mi + 1;
        }
         
        return hi;  // hi refer to the biggest of w which w^2 <= x
    }
    
    /**
     * Solution 2:
     *      here the search was start from 1, like 1, 2, 4, 8, 16, ...
     *      1-st: fast find the range [lo, hi]
     *      2-nd: using binary search to get w
     * @param x
     * @return w
     * @Complexity: O(logn) cause of bin-search
     */
    public static int mySqrt_2(int x) {
        int lo = 0, hi = 1;  // initial range
        
        // find the position range rapidly (exponentially)
        while((long)hi*hi < x) {
            lo = hi;
            hi *= 2;
        }
        
        // using binary search in the range [lo, hi)
        while(lo <= hi) {
            int mi = (lo + hi) >> 1;
            if((long)mi*mi > x) hi = mi - 1;
            else lo = mi + 1;
        }
         
        return hi;  // hi refer to the biggest of w which w^2 <= x
    }
    
    // test code
    public static void main(String[] args) {
        for(int i = 0; i < 20; i++) {
            System.out.println("the sqrt of " + i + " is " + mySqrt_1(i));
        }
        System.out.println("the sqrt of " + 2147395599 + " is " + mySqrt_1(2147395599));
    }

}
