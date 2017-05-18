import java.util.HashSet;
import java.util.Set;

/**
 * @author Peng
 * 
 * Problem Description:
 *      https://leetcode.com/problems/distribute-candies/#/description
 */
public class distribute_candies {

    /**
     * Solution 1:
     *       the maximum number of kinds of candies the sister could gain
     *       is the smaller one of kind number and length/2 of the array.
     * Method:
     *       use hash set -> size for kind calculating.
     * @param candies
     * @return
     */
    public static int distributeCandies(int[] candies) {
        // calculation for kind number
        Set<Integer> kinds = new HashSet<>();
        for (int i : candies) kinds.add(i);
        return kinds.size() < candies.length/2 ? kinds.size(): candies.length/2;        
    }
    
    // test code
    public static void main(String[] args) {
        int[] candies = {1,1,2,3};
        System.out.print(distributeCandies(candies));
    }

}
