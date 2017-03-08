import java.util.HashMap;
import java.util.Map;  // for solution 2

import tree.BinTree;
import tree.BinTree.TreeNode;

/**
 * @author Peng
 * 
 * Problem description:
 *      You are given a binary tree in which each node contains an integer value.
 *      Find the number of paths that sum to a given value.The path does not need 
 *      to start or end at the root or a leaf, but it must go downwards
 *      (traveling only from parent nodes to child nodes).
 *      
 *  for example:
 *      given tree and sum = 8
 *      
 *             10
 *            /  \
 *           5   -3
 *          / \    \
 *         3   2   11
 *        / \   \
 *       3  -2   1
 *       
 *      Return 3. The paths that sum to 8 are:
 *       
 *       1.  5 -> 3
 *       2.  5 -> 2 -> 1
 *       3. -3 -> 11
 *
 */
public class path_sum_III {

    /**
     * Solution 1:
     *      consider using DFS.
     *      as well as add a new value to node for storing the sum from root to there.
     *   for example;
     *      give sum = 8;                  sum = sum-2 
     *      initial tree:   root:      
     *           2            2                 
     *          / \          / \             root.left       root.right   
     *         3   1   ->   3   1      ->        3      ->       1       
     *        / \   \      / \   \              / \               \      
     *       3   2   7    3   2   7            3   2               7     
     *                    |                (all < sum+2)           | 
     *                    |                (no more searching)     |
     *                 [2-3-3]                                  [2-1-7]
     *      return 2;             
     * @param root
     * @param sum
     * @return the number of paths those sum are satisfied
     */
    public static int pathSum1(TreeNode root, int sum) {
        if(root == null)  return 0;
        
        int count = 0;
        count  = pathSum1_rec(root, sum)  // search current root
               + pathSum1(root.left, sum)  // continue searching to next layer
               + pathSum1(root.right, sum);
        
        return count;
    }
    
    /**
     * for DFS recursion
     * @param root
     * @param sum
     */
    public static int pathSum1_rec(TreeNode root, int sum) {
        if (root == null)  return 0;
        int count_rec = 0;
        
        if (sum == root.val)  count_rec++;  //check the current node
        count_rec += pathSum1_rec(root.left, sum - root.val);
        count_rec += pathSum1_rec(root.right, sum - root.val);
        return count_rec;
    }
    
    
    /**
     * Solution 2:
     *      using hashmap to store the prefix sum.
     *      each time check if the any subarray sum to the target, add with some comments:
     * @param root
     * @param sum
     * @return the number of paths those sum are satisfied
     */
    public static int pathSum2(TreeNode root, int sum) {
        if(root == null)  return 0;
        
        Map<Integer, Integer> preSum = new HashMap<>();
        preSum.put(0,1);  // initialization for target key-value
        return pathSum2_recu(root, 0, sum, preSum);
    }
    
    /**
     * for recursive checking the subarray's prefix sum
     * 
     * @param root is the root node of the recursion
     * @param currSum is the current prefix sum of current node
     * @param target 
     * @param preSum
     */
    public static int pathSum2_recu(TreeNode root, int currSum, int target, Map<Integer, Integer> preSum) {
        if (root == null) return 0;
        
        currSum += root.val;
        int count_rec = preSum.getOrDefault(currSum - target, 0);  // find if the is satisfied sum
        preSum.put(currSum, preSum.getOrDefault(currSum, 0) + 1);
        
        count_rec += pathSum2_recu(root.left, currSum, target, preSum)  // continue to next
                   + pathSum2_recu(root.right, currSum, target, preSum);
        preSum.put(currSum, preSum.get(currSum) - 1);
        return count_rec;
    }
       
    public static void main(String[] args) {
        Integer[] data = {10, 5, -3, 3, 2, null, 11, 3, -2, null, 1, null, null, null, null};
        BinTree bt = new BinTree();
        bt.bTreeRoot = bt.createTree(data, 0, 15);  //creating a binary tree.
        
        System.out.println( pathSum1(bt.bTreeRoot, 8) );
        System.out.println( pathSum2(bt.bTreeRoot, 8) );
    }

}
