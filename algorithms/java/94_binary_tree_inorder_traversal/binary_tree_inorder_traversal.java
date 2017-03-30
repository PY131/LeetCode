import java.util.ArrayList;
import java.util.List;
import java.util.Stack;  // for solution 2

import tree.BinTree;
import tree.BinTree.TreeNode;

/**
 * @author Peng 2017/3/30
 * Problem Description:  https://leetcode.com/problems/binary-tree-inorder-traversal/#/description
 *      Given a binary tree, return the inorder traversal of its nodes' values.
 * 
 *      For example:
 *      Given binary tree:
 *         1
 *          \
 *           2
 *          /
 *         3
 *      return [1,3,2].
 *      
 *      Note: Recursive solution is trivial, could you do it iteratively?
 */
public class binary_tree_inorder_traversal {
    
    /**
     * Solution 1:
     *      using recursion
     * @param root
     * @return list of value through inorder traversal
     * 
     * Complexity:
     *      time: O(N)
     */
    public static List<Integer> inorderTraversal_1(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if(root == null)  return res;
        res.addAll(inorderTraversal_1(root.left));
        res.add(root.val);
        res.addAll(inorderTraversal_1(root.right));
        return res;
    }
    
    /**
     * Solution 2:
     *      using stack to realize iteration 
     *      this method can be a little faster than the recursive one
     * @param root
     * @return list of value through inorder traversal
     * 
     * Complexity:
     *      time: O(N)
     */
    public static List<Integer> inorderTraversal_2(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        
        while(stack.empty() != true || root != null){
            if(root != null){
                stack.push(root);
                root = root.left;
            }
            else{
                TreeNode pnode = stack.pop();
                res.add(pnode.val);
                root = pnode.right;
            }
        }
        return res;
    }
    
    public static void main(String[] args) {
        // creating a binary tree.
        Integer[] data = {1, 2, 3, 4, 5, null, null};
        BinTree bt = new BinTree();
        bt.bTreeRoot = bt.createTree(data, 0, 7);  
        
        List<Integer> res = inorderTraversal_2(bt.bTreeRoot);
        
        for(Integer val : res){
            System.out.printf(val + " ");
          }
    }

}
