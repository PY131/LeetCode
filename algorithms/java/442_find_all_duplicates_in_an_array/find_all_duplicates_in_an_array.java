import java.util.ArrayList;
import java.util.List;

/**
 * @author Peng
 * Probelm Description:
 *      Given an array of integers, 1 ¡Ü a[i] ¡Ü n (n = size of array), 
 *      some elements appear twice and others appear once.
 *      Find all the elements that appear twice in this array.
 *      
 *  ps: Could you do it without extra space and in O(n) runtime?
 *      
 *  Example:
 *      Input: [4,3,2,7,8,2,3,1]
 *      Output: [2,3]
 */
public class find_all_duplicates_in_an_array {

    /**
     * Solution 1:
     *      using index = num[i]-1 for check num[i], when 1 ¡Ü a[i] ¡Ü n.
     *      once appear, the nums[index] is set to negative.
     *      twice, the index is duplicate;
     *      
     * @param nums, array of int.
     * @return list of duplicates.
     */
    public static List<Integer> findDuplicates_1(int[] nums) {
        List<Integer> list = new ArrayList<Integer>();
        
        for(int i = 0; i < nums.length; i++) {
            //int index = Math.abs(nums[i]);
            if(nums[Math.abs(nums[i])-1] < 0) list.add(Math.abs(nums[i]));
            else nums[Math.abs(nums[i])-1] = -nums[Math.abs(nums[i])-1];
        }
        
        return list;
    }
    
    // test code
    public static void main(String[] args) {
        int [] num = {4,3,2,7,8,2,3,1};
        List<Integer> list = findDuplicates_1(num);
        
        // print
        for(int i : list) {
            System.out.printf(i + " ");
        }
    }
}
