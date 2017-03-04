
public class minimum_size_subarray_sum {

    /**
     * Problem:
     *      Given an array of n positive integers nums[] and a positive integer s, 
     *      find the minimal length of a contiguous subarray of which the sum ¡Ý s. 
     *      If there isn't one, return 0 instead.
     * 
     * @param s
     * @param nums
     * @return the minimal length of a contiguous subarray of which the sum ¡Ý s. 
     *      If there isn't one, return 0 instead.
     */
    public static int minSubArrayLen(int s, int[] nums) {
        int sum = 0;
        int res = Integer.MAX_VALUE;
        for(int i = 0, j = 0; i < nums.length; i++){
            sum += nums[i];
            while(sum >= s){
                res = Math.min(res, i - j + 1);
                sum -= nums[j++];
            }
        }
        return res == Integer.MAX_VALUE ? 0 : res;   
    }
    
    public static void main(String[] args) {
        int[] nums = {2,3,1,2,4,3};
        int s = 7;
        System.out.print(minSubArrayLen(s, nums));
    }

}
