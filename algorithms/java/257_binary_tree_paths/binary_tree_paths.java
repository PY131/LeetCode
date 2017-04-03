import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

import tree.BinTree;
import tree.BinTree.TreeNode;


/**
 * @author Peng
 * 
 * Problem Discription:
 *      Given a binary tree, return all root-to-leaf paths.
 *      For example, given the following binary tree:
 *               1
 *             /   \
 *            2     3
 *             \
 *              5
 *      All root-to-leaf paths are:
 *           ["1->2->5", "1->3"]
 */
public class binary_tree_paths {

    /**
     * Solution 1:
     *      using iteration
     *      considering stack to realize iteration 
     * @param root
     * @return res: List<String> formed like ["1->2->5", "1->3"]
     */
    public static List<String> binaryTreePaths_1(TreeNode root) {
        List<String> res = new ArrayList<String>();
        if(root == null)  return res;
        
        Stack<String> st_str = new Stack<String>();
        Stack<TreeNode> st_node = new Stack<TreeNode>();
        
        st_str.push("" + root.val);
        st_node.push(root);
        
        while( st_str.empty() != true && st_node.empty() != true ){
            TreeNode p_node = st_node.pop();
            String p_str = st_str.pop();
            if(p_node.left == null && p_node.right == null){
                res.add(p_str);
            }
            else{
                if(p_node.right != null){
                    st_str.push(p_str + "->" + p_node.right.val);
                    st_node.push(p_node.right);
                }
                if(p_node.left != null){
                    st_str.push(p_str + "->" + p_node.left.val);
                    st_node.push(p_node.left);
                }
            }
        }
        return res;
    }
    
    /**
     * Solution 2:
     *      using recursion
     * @param root
     * @return res: List<String> formed like ["1->2->5", "1->3"]
     */
    public static List<String> binaryTreePaths_2(TreeNode root) {
        List<String> res = new ArrayList<String>();  
        if(root == null)  return res;
        recu_fun(root, "", res);
        return res;
    }
        
    // helper function 
    private static void recu_fun(TreeNode root, String str, List<String> res) {
        if(root.left == null && root.right == null) 
            res.add(str + root.val);
        if(root.left  != null)   recu_fun(root.left,  str + root.val + "->", res);
        if(root.right != null)   recu_fun(root.right, str + root.val + "->", res);
    }
    
    public static void main(String[] args) {
        // creating a binary tree.
        Integer[] data = {1, 2, 3, null, 5, null, null};
        BinTree bt = new BinTree();
        bt.bTreeRoot = bt.createTree(data, 0, 7);  
        
        List<String> list = binaryTreePaths_2(bt.bTreeRoot);
        
        for(String str : list){
            System.out.println(str);
        }
        
    }

}
