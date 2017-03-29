import tree.BinTree;
import tree.BinTree.TreeNode;

/**
 * @author Peng 2017/3/29
 * 
 * Problem Description:
 *      Given a binary tree, determine if it is height-balanced.
 *      For this problem, a height-balanced binary tree is defined
 *      as a binary tree in which the depth of the two subtrees
 *      of every node never differ by more than 1.
 */
public class balanced_binary_tree {

    /**
     * Solution 1:
     *      consider recursion directly to get the depth of a root.
     * @param root of the tree
     * @return true if the tree is height-balanced
     * 
     * complexity:
     *      time: O(N^2)
     */
    public static boolean isBalanced_1(TreeNode root) {
        return  ( root == null ) || 
                ( ( root != null ) && 
                    Math.abs( depth(root.left) - depth(root.right) ) <= 1 && 
                    isBalanced_1(root.left) &&
                    isBalanced_1(root.right)
                );
    }
    /**
     * helper function
     * @param root
     * @return the depth of the subtree start from the root
     * 
     * complexity:
     *      time: O(N)
     */
    private static int depth(TreeNode root) {
        if(root == null)  return 0;
        return 1 + Math.max(depth(root.left) , depth(root.right));
    }
    
    /**
     * Solution 2:
     *      using depth() in solution 1's recursive may be slow.
     *      here consider using DFS method
     *  Method:
     *      searching the tree recursively, check each root(subtree) is balanced.
     *        if balanced:return the depth++ of subtree to the upper recursion.   
     *        else:       return -1 to the upper recursion.
     *      
     * @param root of the tree
     * @return true if the tree is height-balanced
     * 
     * complexity:
     *      time: O(N) = O(is_local_balanced())
     */
    public static boolean isBalanced_2(TreeNode root) {
        return is_local_balanced(root) != -1;
    }
    /**
     * helper function for solution 2
     * @param root
     * @return -1 if subtree start from the root isn't balanced.
     *          depth if subtree start from the root is balanced.
     * 
     * complexity:
     *      time: O(N)
     */
    private static int is_local_balanced(TreeNode root) {
        if(root == null)  return 0;  // depth = 0 of leaf node.
        
        int leftDepth = is_local_balanced(root.left);
        if(leftDepth == -1)  return -1;
        int rightDepth = is_local_balanced(root.right);
        if(rightDepth == -1)  return -1;
        
        if(Math.abs(leftDepth - rightDepth) > 1)  return -1;
        return Math.max(leftDepth, rightDepth) + 1;  // depth++ 
    }
    
    // test code
    public static void main(String[] args) {
        // creating a binary tree.
        Integer[] data = {1, 2, 3, 4, 5, null, null};
        BinTree bt = new BinTree();
        bt.bTreeRoot = bt.createTree(data, 0, 7);  
        
        if(isBalanced_2(bt.bTreeRoot))
            System.out.println("the tree is height-balanced.");
        else System.out.println("the tree isn's height-balanced.");
    }

}
