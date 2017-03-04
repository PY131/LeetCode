
/**
 * 
 * @author Peng
 *
 * problem:
 *      Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
 *      For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
 *      the contiguous subarray [4,-1,2,1] has the largest sum = 6.
 *      
 */
public class maximum_subarray {

    /**
     * Analysis:
     *      it seems like a dynamic optimization problem(DP);
     *      so, we need to find out the state transition.
     * Method:
     *      define the maxSum[i] is the max Sum within nums[0] ~ nums[i]
     *      so maxSum[i] = maxSum[i-1] > 0 ? maxSum[i-1] + nums[i] : 0 + nums[i]
     * Complexity:
     *      time: O(N)
     *      space: O(1)
     */
    public static class Solution1 {
        
        /**
         * @param nums is the global array
         * @return max Subarray's sum
         */
        public int maxSubArray(int[] nums) {
            int res = Integer.MIN_VALUE;
            if(nums.length <= 0) return res;
            
            int maxSum = nums[0]; 
            res = maxSum;
            
            for(int i = 1; i < nums.length; i++){
                maxSum = ( maxSum > 0 ? maxSum : 0 ) + nums[i];
                if(res < maxSum) res = maxSum;
            }
            
            return res;
        }
    }
    
    public static void main(String[] args) {
        int nums[] = {-2,1,-3,4,-1,2,1,-5,4};
        
        Solution1 s1 = new Solution1();
        System.out.print( s1.maxSubArray(nums) );
    }

}
