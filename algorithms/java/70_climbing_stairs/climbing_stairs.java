import java.util.Scanner;

/**
 * @author Peng
 * 
 * @Problem Description:
 *     You are climbing a stair case. 
 *     It takes n steps to reach to the top.
 *     Each time you can either climb 1 or 2 steps. 
 *     In how many distinct ways can you climb to the top?
 *   Note: Given n will be a positive integer.
 */
public class climbing_stairs {

    /**
     * Solution 1: using recursion(which seems to be time-consuming)
     * @param n
     * @return the total count of ways
     * 
     * @Complexity: time O(c^n) (exponentially), space O(n)
     */
    public static int climbStairs(int n) {
        if(n <= 0) return 0;
        else if(n == 1) return 1;
        else if(n == 2) return 2;
        else return climbStairs(n-1) + climbStairs(n-2);
    }
    
    /**
     * Solution 2: the answer seem like a Fibonacci sequence.
     *     so we can use dynamic programming (DP)
     *     boundary condition:
     *       f(0) = 1(0 here); f(1) = 1; f(2) = 2; 
     *     recursion (iteration) function: 
     *       f(n) = f(n-1) + f(n-2)
     * @param n
     * @return total count of the ways
     * 
     * @Complexity: time O(n), space O(1)
     */
    public static int climbStairs1(int n) {
        // boundary condition
        if(n <= 0) return 0;
        else if(n == 1) return 1;
        else if(n == 2) return 2;

        // iteration
        int f = 1, g = 2;
        for(int i = 3; i <= n; i++){
            g += f;
            f = g - f;
        }
        return g;
    }
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n;
        while(scan.hasNext()){
            n = scan.nextInt(); 
            System.out.println("the is " + climbStairs1(n) + " ways.");
        }
        scan.close();
    }

}
