/**
 * @author Peng
 * @link 
 *      https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/#/description
 * @Description
 *      Given an array of integers that is already sorted in ascending order, 
 *      find two numbers such that they add up to a specific target number.
 *  
 *      The function twoSum should return indices of the two numbers such 
 *      that they add up to the target, where index1 must be less than index2. 
 *      Please note that your returned answers (both index1 and index2) are
 *      not zero-based.
 *      You may assume that each input would have exactly one solution 
 *      and you may not use the same element twice
 * @Example    
 *      Input: numbers={2, 7, 11, 15}, target=9
 *      Output: index1=1, index2=2
 */
public class two_Sum_II {
    
    /**
     * Solution 3:
     *      using binary search.
     *      fix numbers[i] from i = 0 on, then search j = [i+1] to [n-1] using binary search
     *      to see if the numbers[j] = target - numbers[i] 
     * @param numbers
     * @param target
     * @return integer array of index1 and index2
     * 
     * @Complexity
     *      time O(NlogN)
     */
    public static int[] twoSum_3(int[] numbers, int target) {
        int [] indices = new int[2];
        if (numbers == null || numbers.length < 2) return indices;
        
        for(int i = 0; i < numbers.length; i++) {
            int lo = i + 1, hi = numbers.length - 1; 
            int tar = target - numbers[i];
            while(lo <= hi) {
                int mi = lo + (hi - lo)/2;
                if(numbers[mi] == tar) {
                    indices[0] = i + 1;
                    indices[1] = mi + 1;
                    break;
                }
                else {
                    if(numbers[mi] < tar) lo = mi+1;
                    else hi = mi-1;
                }
            }
        }
        return indices;
    }
    
    /**
     * Solution 2:
     *      calculate from 2 side - numbers[i] & number[j] as i = 0, j = n-1 at beginning.
     *      donate sum = numbers[i] + number[j];
     *      if sum < target, mean i is small, so i++, else j--;
     * @param numbers
     * @param target
     * @return integer array of index1 and index2
     * 
     * @Complexity
     *      time O(N)
     */
    public static int[] twoSum_2(int[] numbers, int target) {
        int [] indices = new int[2];
        if (numbers == null || numbers.length < 2) return indices;
        
        int i = 0, j = numbers.length - 1;
        long sum = numbers[i] + numbers[j];  // long in case of integer overflow
        while(i < j) {
            if(sum == target) { 
                indices[0] = i+1;
                indices[1] = j+1;
                break;
            }
            if(sum < target) i++;
            if(sum > target) j--;
            sum = numbers[i] + numbers[j];
        }
        return indices;
    }

    /**
     * Solution 1:
     *      just brute-force solving
     * @param numbers
     * @param target
     * @return integer array of index1 and index2
     * 
     * @Complexity
     *      time: O(N^2), invalid method
     */
    public static int[] twoSum_1(int[] numbers, int target) {
        int [] indices = new int[2];
        for(int i = 0; i < numbers.length; i++) { 
            for(int j = i + 1; j < numbers.length; j++) {
                if(numbers[i] + numbers[j] == target) {
                    indices[0] = i + 1;
                    indices[1] = j + 1;
                }
            }
        }
        return indices;
    }
    
    // test code
    public static void main(String[] args) {
        int[] nums = {1,2,3,4,4,9,56,90};
        int tar = 8;
        
        long startTime=System.currentTimeMillis();   // get the start time
        int[] indices = twoSum_3(nums, tar);
        long endTime=System.currentTimeMillis(); // get the end time
        System.out.println("indices: " + indices[0] + "," + indices[1]); 
        System.out.println("runtime: " + (startTime - endTime) + "ms");
    }
}
