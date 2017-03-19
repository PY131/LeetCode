import java.util.Scanner;

import tree.BinTree;
import tree.BinTree.TreeNode;

/**
 * @author Peng
 * Problem Description:
 *      Given a binary search tree, write a function kthSmallest 
 *      to find the kth smallest element in it.
 *      
 *      Note: 
 *          You may assume k is always valid, 1 ¡Ü k ¡Ü BST's total elements.
 *          
 *      Follow up:
 *          What if the BST is modified (insert/delete operations) often and you need to
 *          find the kth smallest frequently? How would you optimize the kthSmallest routine?
 *      
 *      Hint:
 *          Try to utilize the property of a BST.
 *          What if you could modify the BST node's structure?
 *          The optimal runtime complexity is O(height of BST).
 */
public class kth_smallest_element_in_a_BST {

    /**
     * Solution 1:
     *      we count the child node numbers and compare to choose sides
     *      and recursive
     * @param root
     * @param k
     * @return 
     */
    public static int kthSmallest_1(TreeNode root, int k) {
        int n = count(root.left);
        
        if(n >= k)  return kthSmallest_1(root.left, k);
        if(n + 1 == k)  return root.val;
        return kthSmallest_1(root.right, k - 1 - n);
    }
    /**
     * count the descendant node number
     * @param root
     * @return descendant node number
     */
    private static int count(TreeNode root) {
        if(root == null) return 0;
        return 1 + count(root.left) + count(root.right);
    }
    
    public static void main(String[] args) {
        // create a binary tree
        Integer[] data = {1, null, 5, null, null, 3, null};
        BinTree bt = new BinTree();
        bt.bTreeRoot = bt.createTree(data, 0, 7);
        
        Scanner scanner = new Scanner(System.in); 
        while (scanner.hasNext()) {
            int n = scanner.nextInt();
            System.out.println("the k-th smallest element is: " + kthSmallest_1(bt.bTreeRoot, n));
        }

        scanner.close();
    }

}
