import java.util.Scanner;

/**
 * @author Peng
 * 
 * You are climbing a stair case. 
 * It takes n steps to reach to the top.
 * Each time you can either climb 1 or 2 steps. 
 * In how many distinct ways can you climb to the top?
 * Note: Given n will be a positive integer.
 *
 */
public class climbing_stairs {

    /**
     * Solution 1: using recursion(which seems to be time-consuming)
     * @param n
     * @return
     */
    public static int climbStairs(int n) {
        if(n <= 0) return 0;
        else if(n == 1) return 1;
        else if(n == 2) return 2;
        else return climbStairs(n-1) + climbStairs(n-2);
    }
    
    /**
     * Solution 2: the answer seem like a Fibonacci sequence.
     *      f(0) = 1(0 here); f(1) = 1; f(2) = 2; 
     *      f(n) = f(n-1) + f(n-2) ... 
     * @param n
     * @return
     */
    public static int climbStairs1(int n) {
        if(n <= 0) return 0;
        else if(n == 1) return 1;
        else if(n == 2) return 2;

        int fpp = 1; //f(n-2) initial to f(1)
        int fp = 2;  //f(n-1) initial to f(2)
        int f = 0;   //f
        for(int i = 3; i <= n; i++){
            f = fpp + fp;
            fpp = fp;
            fp = f;
        }
        return f;
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
