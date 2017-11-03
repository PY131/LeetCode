/**
 * @author Peng
 *
 * @Problem:
 *  Given an array of integers sorted in ascending order, 
 *  find the starting and ending position of a given target value.
 *  Your algorithm's runtime complexity must be in the order of O(log n).
 *  If the target is not found in the array, return [-1, -1].
 *  
 *  For example,
 *      Given [5, 7, 7, 8, 8, 10] and target value 8,
 *      return [3, 4].
 */
public class search_for_a_range {

    /**
     * Solution 1: just use binary search
     *      1-st: find the target, if not return [-1, -1];
     *      2-nd: expanding from the target position to left and right, return the both boundary
     *      
     * @param nums
     * @param target
     * @return [starting position, ending position] 
     * 
     * @Complexity: time: O(logn)
     */
    public static int[] searchRange_1(int[] nums, int target) {
        int lo = 0, hi = nums.length;
        int [] res = {-1, -1};
        
        while(lo < hi) {
            int mi = (lo + hi) >> 1;            
            if(target == nums[mi]) {  // searching to both sides
                int i = mi;  // left searching 
                while(--i >= lo) if(nums[i] != target) break; 
                res[0] = i + 1;
                i = mi;  // right searching 
                while(++i < hi) if(nums[i] != target) break; 
                res[1] = i - 1;
                break;
            }
            else if(target < nums[mi]) hi = mi;
            else lo = mi + 1;
        }
        
        return res;
    }
    
    // test code
    public static void main(String[] args) {
        int [] nums = {5, 7, 7, 8, 8, 10};
        
        int [] res = searchRange_1(nums, 11);
        System.out.printf("the range of target is [%d, %d]", res[0], res[1]);
    }

}
