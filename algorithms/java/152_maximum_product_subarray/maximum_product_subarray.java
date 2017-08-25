/**
 * @author Peng
 * 
 * Problem Description:
 *  Find the contiguous subarray within an array (containing at least one number) 
 *  which has the largest product.
 *  
 *  For example, given the array [2,3,-2,4],
 *  the contiguous subarray [2,3] has the largest product = 6.
 */
public class maximum_product_subarray {

    /**
     * Solution 1:
     * @param nums: the array
     * @return the largest subarray product
     */
    public static int maxProduct(int[] nums) {
        if(nums.length == 0)  return 0;
        int overall_max = nums[0];
        int local_max = overall_max, local_min = overall_max;
        
        for(int i = 1; i < nums.length; i++) {
            int tmp = local_max;
            local_max = Math.max(nums[i], Math.max(nums[i] * local_max, nums[i] * local_min));
            local_min = Math.min(nums[i], Math.min(nums[i] * tmp, nums[i] * local_min));
            if(overall_max < local_max) overall_max = local_max;
        }
        
        return overall_max;
    }
    
    // test code
    public static void main(String[] args) {
        int [] nums = {};
        System.out.println("the largest product is:" + maxProduct(nums));
    }

}
