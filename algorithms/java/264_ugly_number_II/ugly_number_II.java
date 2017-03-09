import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

/**
 * @author Peng
 * 
 * Problem Description:
 *      Write a program to find the n-th ugly number. Ugly numbers are 
 *      positive numbers whose prime factors only include 2, 3, 5. For 
 *      example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the
 *      first 10 ugly numbers.
 *       
 *      Note that 1 is typically treated as an ugly number, and n does
 *      not exceed 1690.
 *      
 */
public class ugly_number_II {

    /**
     * Solution 1:
     *  Idea: 
     *      An ugly number must be multiplied by either 2, 3, or 5 
     *      from a smaller ugly number.
     *      
     *      the ugly numbers list:
     *           L  = 1, 2, 3, 4, 5, 6, 8 ...
     *      set: L1 = 2 * L = 1, 2, 6, 8 ...
     *           L2 = 3 * L = 3, 6, 9, 12 ... 
     *           L3 = 5 * L = 5, 10, 15 ...
     *      st.  L  = mergesort(L1, L2, L3);
     *      
     *      so. set k-th ugly number is U(k);
     *          then U(k) = min(L1, L2, L3) of k-th
     *          
     *  Method:
     *      we can count by L1, L2, L3 in order.
     *      
     * @param n
     * @return the n-th ugly number
     */
    public static int nthUglyNumber_1(int n) {
        int res = 0;    
        List<Integer> l1 = new LinkedList<Integer>();  // for storing the template ugly number
        List<Integer> l2 = new LinkedList<Integer>();    
        List<Integer> l3 = new LinkedList<Integer>();    
        l1.add(1);    
        l2.add(1);    
        l3.add(1); 
        
        for(int i = 0; i < n; i++){
            res = Math.min( Math.min(l1.get(0), l2.get(0)), l3.get(0) );   
            
            //remove the same number of n-th
            if(l1.get(0) == res) l1.remove(0);    
            if(l2.get(0) == res) l2.remove(0);    
            if(l3.get(0) == res) l3.remove(0);    
                
            l1.add(res * 2);    // updating the ugly number list
            l2.add(res * 3);    
            l3.add(res * 5);  
        }
        
        return res;
    }
    
    /**
     * Solution 2:
     *      cause of solution 1 's list operation is a liitle bit slow
     *      so consider of changing the list into array.
     * Idea:
     *      built a array whose length is n to store the ugly number 
     *      from small to large, add 3 index mapping to the array by 
     *      the form of L1, L2, L3.
     * 
     * @param n
     * @return the n-th ugly number
     */
    public static int nthUglyNumber_2(int n) {
        int res = 0;    
        
        int[] ugly_num = new int[n];
        ugly_num[0] = 1;  
        
        int pointer2 = 0;  //mapping the L1 to the array
        int pointer3 = 0;  //mapping the L2 to the array
        int pointer5 = 0;  //mapping the L3 to the array
        
        for(int i = 1, min = 0; i < n; i++){
            min = Math.min( ugly_num[pointer2] * 2, 
                            Math.min( ugly_num[pointer3] * 3, 
                                      ugly_num[pointer5] * 5 ) );    
            
            //remove the same number of n-th
            if(min == ugly_num[pointer2] * 2) pointer2++ ;    
            if(min == ugly_num[pointer3] * 3) pointer3++ ;
            if(min == ugly_num[pointer5] * 5) pointer5++ ;
                
            ugly_num[i] = min;
        }
        return ugly_num[n-1];
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("please input the number's index: "); 
        while(scanner.hasNext()){
            int k = scanner.nextInt();
            System.out.printf("the %d-th ugly number is %d .\n", k, nthUglyNumber_1(k));
            System.out.printf("the %d-th ugly number is %d .\n", k, nthUglyNumber_2(k));
            System.out.println("continue input: "); 
        }
        
        scanner.close();
    }

}
