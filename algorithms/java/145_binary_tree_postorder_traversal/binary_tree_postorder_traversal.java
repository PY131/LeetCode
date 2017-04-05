import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

import tree.BinTree;
import tree.BinTree.TreeNode;

/**
 * @author Peng
 * 
 * Problem Description:
 *      Given a binary tree, return the postorder traversal 
 *      of its nodes' values.(LRD)
 */
public class binary_tree_postorder_traversal {

    /**
     * Solution 1:
     *      using recursion
     * @param root
     * @return value list of LRD
     */
    public static List<Integer> postorderTraversal_1(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if(root == null)  return res;
        res.addAll(postorderTraversal_1(root.left));  //L
        res.addAll(postorderTraversal_1(root.right));  //R
        res.add(root.val);  //D 
        return res;
    }
    
    /**
     * Solution 2:
     *      using iteration
     *      using stack to store the parent node of each step. 
     *      we add info param (boolean) in stack to check the trace-back:
     *          false: trace back from left subtree -> search for right subtree
     *          true: trace back from right subtree -> operation for current root
     *      
     * @param root
     * @return value list of LRD
     */
    public static List<Integer> postorderTraversal_2(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        Stack<TreeNode> st_node = new Stack<TreeNode>();
        Stack<Boolean> st_info = new Stack<Boolean>(); 
        
        while((st_node.empty() != true && st_info.empty() != true) || root != null){
            if(root != null) {
                st_node.push(root);
                st_info.push(false);
                root = root.left;
            }
            else {
                Boolean info = st_info.pop();
                if(info == false) {
                    st_info.push(true);
                    root = st_node.peek().right;
                }
                else res.add(st_node.pop().val);
            }
        }
        
        return res;
    }
    
    public static void main(String[] args) {
        // creating a binary tree.
        Integer[] data = {1, 2, 3, null, 5, null, null};
        BinTree bt = new BinTree();
        bt.bTreeRoot = bt.createTree(data, 0, 7);  
        
        List<Integer> list = postorderTraversal_2(bt.bTreeRoot);
        for(Integer i : list) { 
            System.out.printf(i + "  ");
        }
    }

}
