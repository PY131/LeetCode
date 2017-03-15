import java.util.Scanner;

/**
 * @author Peng
 * 
 * Problem Description:
 *      Given an integer, write a function to determine if 
 *      it is a power of three (such as 1, 3, 9, 27, 81...).
 */
public class power_of_three {

    /**
     * Solution 4:
     *      consider without using any loop or recursion.
     *  idea:
     *     we can use logarithm
     *     log3(n) mast be a natural number if n is the power of 3. 
     *     
     *     log3(n) % 1 == 0;
     *     
     * @param n
     * @return true if n is a power of 3.
     */
    public static boolean isPowerOfThree_4(int n) {
        return (Math.log10(n) / Math.log10(3) ) % 1 == 0;
    }
    
    /**
     * Solution 3:
     *      consider without using any loop or recursion.
     *  idea:
     *      because numbers ( power of 3) are 1,3,9,27... 
     *      which are 1, 1*3, 1*3*3, 1*3*3*3...
     *      set that n(i) = n(i-1) * 3; n(i) % n == 0;
     *      so we can find the biggest n(3^19 = 1162261467) in int (32 bit); 
     *          
     *      n_biggest % n == 0;
     *      
     * @param n
     * @return true if n is a power of 3.
     */
    public static boolean isPowerOfThree_3(int n) {
        return n > 0 && 1162261467 % n == 0;
    }
        
    /**
     * Solution 2:
     *      using loop
     * @param n
     * @return true if n is a power of 3.
     */
    public static boolean isPowerOfThree_2(int n) {
        while(n >= 3){
            if(n%3 != 0)  return false;
            n = n/3;
        }
        if(n == 1)  return true;
        return false;
    }
    
    /**
     * Solution 1:
     *      using recursion
     * @param n
     * @return true if n is a power of 3.
     */
    public static boolean isPowerOfThree_1(int n) {
        if(n <= 0)  return false;
        if(n == 1)  return true;
        if(isPowerOfThree_1(n/3) == true && n%3 == 0)  return true;
        return false;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while(scanner.hasNext()){
            int n = scanner.nextInt();
            if(isPowerOfThree_4(n)) {
                System.out.printf("%d is the power of 3. \n", n );
            }
            else {
                System.out.printf("%d isn't the power of 3. \n", n );
            }
        }
        scanner.close();
    }

}
