import java.util.Arrays;

/**
 * @author Peng
 * 
 * @see
 *      https://leetcode.com/problems/array-partition-i/#/description
 *      
 * @Problem_Description
 * 
 *      Given an array of 2n integers, 
 *      your task is to group these integers into n pairs of integer, 
 *      say (a1, b1), (a2, b2), ..., (an, bn) 
 *      which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
 *      
 *   Example 1:
 *   
 *      Input: [1,4,3,2]
 *      Output: 4
 *      Explanation: n is 2, and the maximum sum of pairs is 4.
 *      
 *   Note:
 *   
 *      n is a positive integer, which is in the range of [1, 10000].
 *      All the integers in the array will be in the range of [-10000, 10000].
 */
public class array_partition_I {

    /**
     * @param nums: int, array of numbers.
     * @return sum_max: int, maximum sum of pairs in this array.
     * 
     * @Solution_1_idea
     *      when the array is sorted as nums = [a1, b1, a2, b2, ..., an, bn]
     *      the pairs is selected from small to big by every 2 numbers,
     *      formed as [(a1, b1), (a2, b2), ..., (an, bn)],
     *      then the sum of min(ai, bi) is maximum.
     *      
     * @Complexity using rapid sorting
     *      time:   O(NlgN)
     *      space:  O(NlgN)
     */
    public static int arrayPairSum_1(int[] nums) {
        int sum_max = 0;
        
        Arrays.sort(nums);
        for(int i = 0; i < nums.length; i += 2 ) {
            sum_max += nums[i];
        }
        
        return sum_max;
    }
        
    /**
     * @param nums: int, array of numbers.
     * @return sum_max: int, maximum sum of pairs in this array.
     * 
     * @Solution_2_idea
     *      expands from Solution_1 (arrayPairSum_1).
     *      the sort() operation is two time-consuming (O(NlgN))
     *      here we construce a new array to store the count of nums[i] in index of i+10000 (Note)
     *      using this count array to calculating by every two number
     *   notes: 
     *      this solution may be effective when array is large. (trade space for time)
     *      
     * @Complexity
     *      time:   O(N)
     *      space:  O(N)
     */
    public static int arrayPairSum_2(int[] nums) {
        int sum_max = 0;
        int[] count = new int[20001];  // using byte for space saving
        
        for(int i = 0; i < nums.length; i++ ) {
            count[nums[i]+10000]++;  // add 10000 for negatives. via this way, the nums[] is sorted 
        }
        
        boolean odd = true;  // for repeat 
        for(int i = 0; i < 20001; i++) {
            while (count[i] > 0) {  // numbers existed
                if (odd) {
                    sum_max += i - 10000;
                }
                odd = !odd;  // add to sum by every 2 numbers
                count[i]--;
            }            
        }

        return sum_max;
    }
          
    
    // test code
    public static void main(String[] args) {
        int[] nums_test = {1,2,3,4,5,6,7,8};
        System.out.println("the max sum is:" + arrayPairSum_2(nums_test));
    }

}
