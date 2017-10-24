/**
 * @author Peng
 *
 * Problem Description:
 *     Count the number of prime numbers less than a non-negative number, n.
 */
public class count_primes {

    /**
     * Solution 1: using 'Sieve of Eeatosthese' method
     * @return the number of prime number less than n
     */
    public static int count_primes(int n){
        if(n <= 1)  return 0;
        
        int count = 0;
        boolean [] flag = new boolean[n];  // mark flag to see whether the number has been marked to be 1
        for(int i = 2; i < n; i++) {
            if(!flag[i]) {
                count++;  // i is a prime
                for(int j = 2; i*j < n; ++j)  flag[i*j] = true;  // adjust the flag
            }
        }
        
        return count;
    }
    
    public static void main(String[] args) {
        System.out.println(count_primes(7));
    }

}
