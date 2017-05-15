import java.util.Arrays;

/**
 * @author Peng
 * 
 * Problem Description:
 *      https://leetcode.com/problems/reshape-the-matrix/#/description
 */
public class reshape_the_matrix {
    
    /**
     * Solution 1:
     *      here we just using index from nums[r0][c0] to res[r][c]
     *      for nums[i][j], the nums index is n = i*c0+j;
     *      assign to res[][], the row = n/c, column = n%c;
     * 
     * @param nums is the raw matrix
     * @param r,c is the matrix size after reshape
     * @return res, reshaped matrix
     */
    public static int[][] matrixReshape(int[][] nums, int r, int c) {
        int r0 = nums.length;
        int c0 = nums[0].length;
        
        if(r0*c0 != r*c) return nums;   // judge if reshaping is possible

        int[][] res = new int[r][c];
        for(int i = 0; i < r0; i++) 
            for(int j = 0; j < c0; j++)
                res[(i*c0+j)/c][(i*c0+j)%c] = nums[i][j];
        
        return res;    
    }
    
    // test code
    public static void main(String[] args) {
        int[][] nums ={{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15}};
        int[][] res = matrixReshape(nums, 5, 3);
        
        System.out.println(Arrays.deepToString(res));  
    }
}
