import java.util.TreeSet;

import tree.BinTree;
import tree.BinTree.TreeNode;

/**
 * @author Peng
 * 
 * Problem Description
 *  Given a binary search tree with non-negative values, 
 *  find the minimum absolute difference between values of any two nodes.
 *  
 *  for example:
 *       
 *       Input:
 *       
 *          1
 *           \
 *            3
 *           /
 *          2
 *       
 *       Output:
 *       1
 *
 *       Explanation:
 *       The minimum absolute difference is 1, which is the difference 
 *       between 2 and 1 (or between 2 and 3).
 *  
 */
public class minimum_absolute_difference_in_BST {

    static int current_min = Integer.MAX_VALUE;
    static Integer prev_val = null;  // from most left(smallest) to most right(biggest)
    
    /**
     * Solution 1:
     *      using in-order traversal
     * idea:
     *      because the BST' node value are sorted.
     *      
     * @param root of BST
     * @return the minimum absolute difference between values of any two nodes.
     */
    public static int getMinimumDifference_1(TreeNode root) {
        if(root == null)  return current_min;  
        
        getMinimumDifference_1(root.left);  // recursive to the smallest node
        if(prev_val != null) 
            current_min = Math.min(current_min, root.val - prev_val);
        prev_val = root.val;  // from left to right
        getMinimumDifference_1(root.right);
        
        return current_min;
    }
    
    /**
     * Solution 2:
     *      we could put value in a treeset so the problem can be solved whether
     *      the tree is a BST.
     *      
     * @param root of BST
     * @return the minimum absolute difference between values of any two nodes.
     */
    
    static TreeSet<Integer> set = new TreeSet<>();
    
    public static int getMinimumDifference_2(TreeNode root) {
        if(root == null)  return current_min;  
        
        if (!set.isEmpty()) {
            if (set.floor(root.val) != null) {
                current_min = Math.min(current_min, Math.abs(root.val - set.floor(root.val)));
            }
            if (set.ceiling(root.val) != null) {
                current_min = Math.min(current_min, Math.abs(root.val - set.ceiling(root.val)));
            }
        }
        
        set.add(root.val);
        
        getMinimumDifference_2(root.left);
        getMinimumDifference_2(root.right);
  
        return current_min;
    }

    public static void main(String[] args) {
        // create a binary tree
        Integer[] data = {1, null, 5, null, null, 3, null};
        BinTree bt = new BinTree();
        bt.bTreeRoot = bt.createTree(data, 0, 7);
        
        System.out.println(getMinimumDifference_2(bt.bTreeRoot));
        
    }

}
