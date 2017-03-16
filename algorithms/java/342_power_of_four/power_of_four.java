import java.util.Scanner;

/**
 * @author Peng
 * 
 * Problem Description:
 *      Given an integer (signed 32 bits), write a function 
 *      to check whether it is a power of 4.
 *      
 *  for example:
 *      Given num = 16, return true. 
 *      Given num = 5, return false.
 */
public class power_of_four {

    /**
     * Solution 1:
     *      the power of four's num have these features:
     *      1. num > 0;
     *      2. num have only one 1-bit in odd position:
     *          such as: 1  - ..00000001
     *                   4  - ..00000100
     *                   16 - ..00010000
     *                   64 - ..01000000
     *                   
     *      so we can get our method:
     *      1. num > 0;
     *      2. num & (num - 1) to check it has only one 1-bit;
     *      3. num & 0x55555555 to check the 1-bit in odd position;
     *      
     * @param num
     * @return true if n is a power of 4.
     */
    public static boolean isPowerOfFour_1(int num) {
        return num > 0 && (num & (num - 1)) == 0 && (num & 0x55555555) != 0;
    }
    
    /**
     * Solution 2:
     *      extends from solution 1.
     *      consider: 4^n-1 = (2^n-1)*(2*n+1);
     *                there must exist on number is the power of three
     *                among three consecutive numbers: (2^n-1),(2n),(2*n+1)
     *                
     *      another consider: 
     *                (4^n-1) = (4-1)(4^(n-1) + 4^(n-2) + 4^(n-3) + ..... + 4 + 1)
     *                
     *      but the power of 2 does not have such feature(n-1) is the multiple of 3.
     *      
     * @param num
     * @return true if n is a power of 4.
     */
    public static boolean isPowerOfFour_2(int num) {
        return num > 0 && (num & (num - 1)) == 0 && (num - 1) % 3 == 0;
    }
    
    /**
     * Solution 3:
     *      refer to the "power of 3" solution 4.
     *      we can use logarithm to check whether is the power of 4.
     *      
     * @param num
     * @return true if n is a power of 4.
     */
    public static boolean isPowerOfFour_3(int num) {
        return (Math.log10(num) / Math.log10(4) ) % 1 == 0;
    }
    
    // test code
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while(scanner.hasNext()){
            int n = scanner.nextInt();
            if(isPowerOfFour_2(n)) {
                System.out.printf("%d is the power of 4. \n", n );
            }
            else {
                System.out.printf("%d isn't the power of 4. \n", n );
            }
        }
        scanner.close();
    }

}
