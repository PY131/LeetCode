import java.math.BigDecimal;
import java.util.Scanner;

import tree.BinTree;
import tree.BinTree.TreeNode;

/**
 * @author Peng
 * 
 * Problem Description:
 *     Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST. 
 *     According to the definition of LCA on Wikipedia: ¡°The lowest common ancestor is defined 
 *     between two nodes v and w as the lowest node in T that has both v and w as descendants 
 *     (where we allow a node to be a descendant of itself).¡±
 *     
 * for example:
 *       _______6______
 *      /              \
 *   ___2__          ___8__
 *  /      \        /      \
 *  0      _4       7       9
 *        /  \
 *        3   5
 *     the lowest common ancestor (LCA) of nodes 2 and 8 is 6. 
 *     Another example is LCA of nodes 2 and 4 is 2, 
 *     since a node can be a descendant of itself according to the LCA definition.
 */
public class lowest_common_ancestor_of_a_binary_search_tree {

    /**
     * Solution 1: 
     *      consider using recursion
     *      assume p > q, if q <= node <= p, it is the LCA 
     * 
     * @param root
     * @param p
     * @param q
     * @return the LCA node
     */
    public static TreeNode lowestCommonAncestor_1(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode res = null;
        
        // p is bigger than q
        if(p.val > q.val) {
            if(root.val > p.val) res = lowestCommonAncestor_1(root.left, p, q);
            else if(root.val < q.val) res = lowestCommonAncestor_1(root.right, p, q);
            else if(root.val >= q.val && root.val <= p.val) return root;
        }
        
        // p is no bigger than q
        else if(p.val <= q.val) {
            if(root.val > q.val) res = lowestCommonAncestor_1(root.left, p, q);
            else if(root.val < p.val) res = lowestCommonAncestor_1(root.right, p, q);
            else if(root.val >= p.val && root.val <= q.val) return root;
        }
    
        return res;
    }
    
    /**
     * Solution 2: 
     *      little change from solution 1 
     * 
     * @param root
     * @param p
     * @param q
     * @return the LCA node
     */
    public static TreeNode lowestCommonAncestor_2(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode res = null;
        
        if(p.val > q.val) res = lowestCommonAncestor(root, p, q);
        else res = lowestCommonAncestor(root, q, p);
       
        return res;
    }
    
    // helper function for lowestCommonAncestor_2()
    // assert the p > q
    public static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode res = null;
        
        if(root.val > p.val) res = lowestCommonAncestor(root.left, p, q);
        else if(root.val < q.val) res = lowestCommonAncestor(root.right, p, q);
        else if(root.val >= q.val && root.val <= p.val) res = root;
        
        return res;
    }
    
    // test code
    public static void main(String[] args) {
        // create a binary tree
        Integer[] data = {4, 2, 6, 1, 3, 5, 7};
        BinTree bt = new BinTree();
        bt.bTreeRoot = bt.createTree(data, 0, 7);
        
        TreeNode root = bt.bTreeRoot;  // root.val = 4
        TreeNode p = root.left.left;  // p.val = 1
        TreeNode q = root.left.right;   // p.val = 3
        
        System.out.println("the LCA's value is " + lowestCommonAncestor_2(root, p, q).val);
    }

}
