import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

import tree.BinTree;
import tree.BinTree.TreeNode;

/**
 * @author Peng
 * 
 * Problem Description:
 *      Given a binary tree, return the preorder traversal 
 *      of its nodes' values.(DLR)
 */
public class binary_tree_preorder_traversal {

    /**
     * Solution 1:
     *      using recursive
     * @param root
     * @return nodes' values list of DLR
     */
    public static List<Integer> preorderTraversal_1(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if(root == null)  return res;
        res.add(root.val);
        res.addAll(preorderTraversal_1(root.left));
        res.addAll(preorderTraversal_1(root.right));
        
        return res;
    }
    
    /**
     * Solution 2:
     *      using iteration
     * @param root
     * @return nodes' values list of DLR
     */
    public static List<Integer> preorderTraversal_2(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        Stack<TreeNode> st = new Stack<TreeNode>();
        
        while(st.empty() != true || root != null){
            if(root != null) {
                res.add(root.val);
                st.push(root);
                root = root.left;
            }
            else {
                root = st.pop().right;
            }
        }
        
        return res;
    }
    
    
    public static void main(String[] args) {
        // creating a binary tree.
        Integer[] data = {1, 2, 3, null, 5, null, null};
        BinTree bt = new BinTree();
        bt.bTreeRoot = bt.createTree(data, 0, 7);  
        
        List<Integer> list = preorderTraversal_2(bt.bTreeRoot);
        for(Integer i : list) { 
            System.out.printf(i + "  ");
        }
    }

}
