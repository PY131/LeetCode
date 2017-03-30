import tree.BinTree;
import tree.BinTree.TreeNode;

/**
 * @author Peng 2017/3/30
 *
 * Problem Description: https://leetcode.com/problems/minimum-depth-of-binary-tree/#/description
 *     
 *     Given a binary tree, find its minimum depth.
 *     The minimum depth is the number of nodes along the shortest 
 *     path from the root node down to the nearest leaf node. 
 * 
 */
public class minimum_depth_of_binary_tree {

    /**
     * Solution 1:
     *      just using recursion
     * @param root
     * @return
     */
    public static int minDepth(TreeNode root) {
        if(root == null)  return 0;
        if(root.left == null) return 1 + minDepth(root.right);
        if(root.right == null) return 1 + minDepth(root.left);
        return 1 + Math.min(minDepth(root.left) , minDepth(root.right));
    }
    
    // test code
    public static void main(String[] args) {       
        // creating a binary tree.
        Integer[] data = {1, 2, 3, 4, 5, null, null};
        BinTree bt = new BinTree();
        bt.bTreeRoot = bt.createTree(data, 0, 7);  
        
        System.out.println("the minimum depth is: " + minDepth(bt.bTreeRoot));
    }

}
