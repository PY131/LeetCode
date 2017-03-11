import java.util.Scanner;

/**
 * @author Peng
 * 
 * Problem Description:
 *      Given a non negative integer number num. For every numbers i in
 *      the range 0 ¡Ü i ¡Ü num calculate the number of 1's in their binary
 *      representation and return them as an array.
 *      
 *  For Example:
 *      For num = 5 you should return [0,1,1,2,1,2].
 *      
 * Idea:
 *      it seems like a bitcount problem.
 *      and there may have some small tricks.
 */
public class counting_bits {

    /*********************************************************
     * Solution 1: using Integer.bitCount()
     *      
     * @param num an negative integer
     * @return the array of 1 bit's numbers in there binary
     */
    public static int[] countBits_1(int num) {
        int[] res = new int[num + 1];
        for(int i = 0; i <= num; i++) res[i] = Integer.bitCount(i);
        return res;
    }
    
    /***********************************************************
     * Solution 2: using MIT HAKMEM Algorithm for bitCount
     *      
     * @param num an negative integer
     * @return the array of 1 bit's numbers in there binary
     */
    public static int[] countBits_2(int num) {
        int[] res = new int[num + 1];
        for(int i = 0; i <= num; i++) res[i] = Hakmem_bitCount(i);
        return res;
    }
    
    private static int Hakmem_bitCount(int x) {  
        int n;     
        n = (x >> 1) & 033333333333;     
        x = x - n;    
        n = (n >> 1) & 033333333333;    
        x = x - n;     
        x = (x + (x >> 3)) & 030707070707;       
        x = x%63;     
        return x;      
    } 
    
    /***********************************************************
     * Solution 3: looking at this problem, it asks us to calculate an array
     *             based on an number's sequence 0, 1, 2, 3 ... num.
     *             so, we may use the result of previous for current number.
     *      Method:
     *             bitcount(i) = bitcount(i/2) + bitcount(i%2) 
     *                         = bitcount(i/2) + i%2
     *             st we have only need to calculate the 1/2 and i%2 without 
     *             bit operation
     *             
     *      Complexity:
     *             time:    O(N)
     *             space:   O(N);    
     * 
     * @param num an negative integer
     * @return the array of 1 bit's numbers in there binary
     */
    public static int[] countBits_3(int num) {
        int[] res = new int[num + 1];
        for(int i = 0; i <= num; i++) res[i] = res[i/2] + i%2;
        return res;
    }
    
    /***********************************************************
     * for runtime monitoring (unit: ms)
     */
    public static long elapsedTime(long start) {
        long now = System.currentTimeMillis();
        return (now - start);
    }
    
    public static void main(String[] args) {
        long start;  // for runtime monitor
        
        Scanner scan = new Scanner(System.in);
        
        System.out.println("input an positive integer :");
        while(scan.hasNext()) {
            int num = scan.nextInt();
            
            start = System.currentTimeMillis(); 
            System.out.println("using solution 1:");
            for(int i : countBits_1(num)) {
                System.out.printf(i + " ");
            }
            System.out.println();
            System.out.println("runtime:" + elapsedTime(start) + " ms");
            
            start = System.currentTimeMillis(); 
            System.out.println("using solution 2:");
            for(int i : countBits_2(num)) {
                System.out.printf(i + " ");
            }
            System.out.println();
            System.out.println("runtime:" + elapsedTime(start) + " ms");
            
            start = System.currentTimeMillis();             
            System.out.println("using solution 3:");
            for(int i : countBits_3(num)) {
                System.out.printf(i + " ");
            }
            System.out.println();
            System.out.println("runtime:" + elapsedTime(start) + " ms");
            
            System.out.println("continue inputing :");
        }
        
        scan.close();
    }
}
