/**
 * @author Peng
 *
 * Problem: 
 *      Given a m x n grid filled with non-negative numbers, 
 *      find a path from top left to bottom right which 
 *      minimizes the sum of all numbers along its path. 
 *      
 *      Note: You can only move either down or right at any point in time.
 */
public class minimum_path_sum {

    /**
     * Solution 1:
     * 
     * @idea:
     *     1. state: 
     *          min_sum(i,j): the min_sum to grid[i][j]
     *     2. state transition:
     *          min_sum(i+1,j+1) = min{ min_sum(i+1,j), min_sum(i,j+1) } + grid[i+1][j+1]
     *     3. initial:
     *          min_sum(0,0) = grid[0][0]
     *     4. goal:
     *          min_sum(m-1,n-1)
     *          
     * @method:
     *     using DP, here we need a assist matrix to store the result for each node;
     *     
     * @param grid£ºint matrix.
     * @return int, min path sum.
     */
    public static int minPathSum_1(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        if(m == 0 || n == 0) return 0; 
        
        // construct assist matrix
        int [][]min_sum = new int[m][n];
        
        // forward conduction
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++) {
                // 1-st item
                if(i == 0 && j == 0)  min_sum[i][j] = grid[i][j];
                // 1-st row
                else if(i == 0) min_sum[i][j] = min_sum[i][j-1] + grid[i][j];
                // 1-st column
                else if(j == 0) min_sum[i][j] = min_sum[i-1][j] + grid[i][j];    
                // common row and column
                else min_sum[i][j] = Math.min(min_sum[i][j-1], min_sum[i-1][j]) + grid[i][j];
            }
        
        return min_sum[m-1][n-1];
    }
    
    // test code
    public static void main(String[] args) {
        int[][] grid = {{1,2,3,4},{5,6,7,8},{9,10,11,12}};
        System.out.println("the min path sum is: " + minPathSum_1(grid));
    }

}
