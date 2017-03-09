import java.util.Scanner;

/**
 * @author Peng
 * 
 * Problem Description:
 *      Write a program to check whether a given number is an ugly number.
 *      Ugly numbers are positive numbers whose prime factors only include 
 *      2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it 
 *      includes another prime factor 7.
 *      
 *      Note that 1 is typically treated as an ugly number.
 *        
 */
public class ugly_number {
    
    /**
     * Solution 1:
     *      using "Pollard Rho Algorithms"
     *      (a method of fast decomposition of the quality factor)
     * @param num
     * @return true if the number is an ugly number.
     */
    public static boolean isUgly1(int num) {
        if(num <= 0) return false;
        if(num == 1) return true;
        
        for(int i = 2; i <= num; ) {   
            if(num % i == 0){
                if(i > 5)  return false;  // is a factor but not 2, 3, 5
                num /= i;  //is an ugly factor and continue 
            }
            else{
                if(i++ > 5)  return false;  //must not ugly factor, no need for more 
                continue;  // not a factor
            }
        }
        return true;
    }
    
    
    /**
     * Solution 2:
     *      extension from solution 1
     * @param num
     * @return true if the number is an ugly number.
     */
    public static boolean isUgly2(int num) {
        if(num <= 0) return false;
        if(num == 1) return true;
        
        while(true){  
            if(num % 2 == 0) num /= 2;  
            else if(num % 3 == 0) num /= 3;  
            else if(num % 5 == 0) num /= 5;  
            else return num == 1;  // if not, means there are bigger quality factor than 5
        }  
    }
    
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("please input the number: "); 
        while(scanner.hasNext()){
            int k = scanner.nextInt();
            System.out.println("is ugly number? (0 = no, 1 = yes): " + isUgly1(k));
            System.out.println("is ugly number? (0 = no, 1 = yes): " + isUgly2(k));
            System.out.println("continue input: "); 
        }
        
        scanner.close();
    }

}
