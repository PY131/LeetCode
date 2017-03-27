import tree.BinTree;
import tree.BinTree.TreeNode;

/**
 * @author Peng
 * 
 * 543. Diameter of Binary Tree
 * 
 * Problem Description:  https://leetcode.com/problems/diameter-of-binary-tree/#/description
 * 
 *      Given a binary tree, you need to compute the length of the diameter of the tree. 
 *      The diameter of a binary tree is the length of the longest path between any two 
 *      nodes in a tree. This path may or may not pass through the root.
 *
 * Example:
 *      Given a binary tree 
 *                1
 *               / \
 *              2   3
 *             / \     
 *            4   5    
 *      Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
 *      
 *      Note: The length of path between two nodes is represented 
 *      by the number of edges between them.
 */
public class diameter_of_binary_tree {

    /**
     * Solution 1:
     *      using recursion
     * @param root
     * @return the diameter of the tree 'root'
     */
    public static int diameterOfBinaryTree_1(TreeNode root) {
        if(root == null)  return 0;
        return Math.max(depth(root.left) + depth(root.right) ,
                        Math.max(diameterOfBinaryTree_1(root.left) , 
                                 diameterOfBinaryTree_1(root.right)) );
    }
    
    /**
     * helper function
     * @param root
     * @return the depth of the subtree start from the root
     */
    private static int depth(TreeNode root) {
        if(root == null)  return 0;
        return 1 + Math.max(depth(root.left) , depth(root.right));
    }
    
    // test code
    public static void main(String[] args) {
        // creating a binary tree.
        Integer[] data = {1, 2, 3, 4, 5, null, null};
        BinTree bt = new BinTree();
        bt.bTreeRoot = bt.createTree(data, 0, 7);  
        
        System.out.println("the diameter of the tree is: " + diameterOfBinaryTree_1(bt.bTreeRoot));
    }

}
