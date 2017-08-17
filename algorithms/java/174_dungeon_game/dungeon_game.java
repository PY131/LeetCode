
/** 
 * @author Peng
 *
 * @Description:
 *      The demons had captured the princess (P) and imprisoned her 
 *      in the bottom-right corner of a dungeon. The dungeon consists 
 *      of M x N rooms laid out in a 2D grid. Our valiant knight (K) 
 *      was initially positioned in the top-left room and must fight
 *      his way through the dungeon to rescue the princess.
 *      
 *      The knight has an initial health point represented by a positive integer. 
 *      If at any point his health point drops to 0 or below, he dies immediately.
 *      
 *      Some of the rooms are guarded by demons, so the knight loses health (negative integers) 
 *      upon entering these rooms; other rooms are either empty (0's) or contain magic orbs 
 *      that increase the knight's health (positive integers).
 *      
 *      In order to reach the princess as quickly as possible, the knight decides 
 *      to move only rightward or downward in each step.
 *      
 *      Write a function to determine the knight's minimum initial health so that 
 *      he is able to rescue the princess.
 */

public class dungeon_game {
    
    /**
     * Solution 1:
     *      using DP:
     * @method:
     *      1. state: 
     *          h(i,j) - is the min health require when entering dungeon[i][j] (after surviving in former rooms)
     *      2. state transition:
     *          h(i,j) = min( h(i+1,j) - dungeon[i+1][j],    // down 
     *                        h(i,j+1) - dungeon[i][j+1]     // right
     *                
     * @param dungeon
     * @return
     */
    public static int calculateMinimumHP(int[][] dungeon) {
        int m = dungeon.length;
        int n = dungeon[0].length;
        if(m == 0 || n == 0)  return 0;
        int [][] h = new int[m][n];
        for(int i = m-1; i >= 0; i--)
            for(int j = n-1; j >= 0; j--) {
                if(i == m-1 && j == n-1) { 
                    h[m-1][n-1] = Math.max(1 - dungeon[i][j], 1) ;  // health must no less than 1 
                    continue;
                }
                else if(i == m-1)  h[i][j] = Math.max(h[i][j+1] - dungeon[i][j], 1);  // last row
                else if(j == n-1)  h[i][j] = Math.max(h[i+1][j] - dungeon[i][j], 1);  // last column
                else h[i][j] = Math.max(Math.min(h[i][j+1], h[i+1][j]) - dungeon[i][j], 1);
            }
        return h[0][0];
    }
    
    // test code
    public static void main(String[] args) {
        int[][] dungeon = {{1,2,-3,-4},{-5,6,-7,8},{-9,10,-11,-12}};
        System.out.println("the min initial health is:" + calculateMinimumHP(dungeon));
    }

}
