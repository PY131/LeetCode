/**
 * @author Peng
 * 
 * @Problem:
 *  Given a sorted array and a target value, return the index if the target is found. 
 *  If not, return the index where it would be if it were inserted in order.
 *  You may assume no duplicates in the array.
 *  
 *  Here are few examples.
 *      [1,3,5,6], 5 ¡ú 2
 *      [1,3,5,6], 2 ¡ú 1
 *      [1,3,5,6], 7 ¡ú 4
 *      [1,3,5,6], 0 ¡ú 0
 */
public class search_insert_position {
        
    /**
     * Solution 1: check in order directly
     * @param nums
     * @param target
     * @return the insert index of target in nums 
     */
    public static int searchInsert1(int[] nums, int target) {
        int i;
        for(i = 0; i < nums.length; i++){
            if(nums[i] < target) continue;
            else return i;
        }
        return i;
    }
 
    /**
     * Solution 2: using Binary-Search
     * @param nums
     * @param target
     * @return the insert index of target in nums 
     */
    public static int searchInsert2(int[] nums, int target) {
        int max = nums.length - 1, min = 0, mid;
        while(min <= max){
            mid = (max + min) / 2;
            if(nums[mid] == target) return mid;
            else if(nums[mid] > target) max = mid - 1;
            else min = mid + 1;
        }
        return min;
    }
    
    /**
     * Solution 3: another Binary-Search (a little modify)
     * 
     * @param nums
     * @param target
     * @return the insert index of target in nums 
     * 
     * @Complexity: time O(logn)
     */
    public static int searchInsert3(int[] nums, int target) {
        int lo = 0, hi = nums.length;  // search the target in [lo, hi)
        
        while(lo < hi) {
            int mi = (lo + hi) >> 1;  // middle point index
            if(target < nums[mi]) hi = mi;
            else lo = mi + 1;
        }
        return (lo == 0) ? lo : (target == nums[lo-1]) ? lo-1 : lo;
    }
    
    // test code
    public static void main(String[] args) {
        int nums[] = {1,2,3,5,6};
        int target = 8;
        
        System.out.print( searchInsert3(nums, target) );
    }

}
