
public class search_insert_position {

    /**
     * Solution 1: check in order directly
     */
    public static class Solution1 {
        
        /**
         * @param nums
         * @param target
         * @return the insert index of target in nums 
         */
        public int searchInsert(int[] nums, int target) {
            int i;
            for(i = 0; i < nums.length; i++){
                if(nums[i] < target) continue;
                else return i;
            }
            return i;
        }
    }
    
    /**
     * Solution 2: using Binary-Search
     */
    public static class Solution2 {
        
        /**
         * @param nums
         * @param target
         * @return the insert index of target in nums 
         */
        public int searchInsert(int[] nums, int target) {
            int max = nums.length - 1, min = 0, mid;
            while(min <= max){
                mid = (max + min) / 2;
                if(nums[mid] == target) return mid;
                else if(nums[mid] > target) max = mid - 1;
                else min = mid + 1;
            }
            return min;
        }
    }
    
    public static void main(String[] args) {
        int nums[] = {1,2,3,4,5};
        int target = 7;
        
        Solution1 s1 = new Solution1();
        System.out.print( s1.searchInsert(nums, target) );
        Solution2 s2 = new Solution2();
        System.out.print( s2.searchInsert(nums, target) );
    }

}
