import java.util.Scanner;

/**
 * @author Peng
 * 
 * @Problem_Description:
 *      Given a positive integer n, find the least number of perfect square numbers 
 *      (for example, 1, 4, 9, 16, ...) which sum to n.
 *  
 *  For example, 
 *      given n = 12, return 3 because 12 = 4 + 4 + 4; 
 *      given n = 13, return 2 because 13 = 4 + 9.
 */
public class perfect_squares {

    /**
     * solution 1:
     *  idea:
     *      set dp[n] is the target number of given n
     *      so. dp[0] = 0
     *          dp[1] = 1 = min( dp[1-1*1] )+1
     *          dp[2] = 1 + 1 = 2 = min( dp[2-1*1] )+1
     *          dp[3] = 1 + 1 + 1 = 3 = min( dp[3-1*1] )+1
     *          dp[4] = min( dp[4-1*1], dp[4-2*2] )+1
     *          dp[5] = min( dp[5-1*1], dp[5-2*2] )+1
     *          ...
     *          dp[9] = min( dp[9-1*1], dp[9-2*2], dp[9-3*3] )+1
     *          ...
     *  so the iterative function can be listed out
     *  
     * @param n
     * @return least number of perfect square numbers
     * 
     * @Complexity: time: O(n^2), space: O(n)
     */
    public static int numSquares_1(int n) {
        // initial
        int [] dp = new int[n+1];
        dp[0] = 0;
        
        // iteration
        for(int i = 1; i < n+1; i++) {
            int min = dp[i-1];
            for(int j = 2; j*j <= i; j++) {
                if(dp[i-j*j] < min) min = dp[i-j*j];
            }
            dp[i] = min + 1;
        }
        
        // get result
        return dp[n];
    }
    
    // test code
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n;
        while(scan.hasNext()){
            n = scan.nextInt(); 
            System.out.println("the least number of " + n + " is " + numSquares_1(n));
        }
        scan.close();
    }

}
