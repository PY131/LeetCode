import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

import tree.BinTree;
import tree.BinTree.TreeNode;

/**
 * @author Peng
 * 
 * Problem description:
 *      Given a binary tree and a sum, find all root-to-leaf paths 
 *      where each path's sum equals the given sum.
 *      
 *   For example:
 *      Given the below binary tree and sum = 22,
 *             5
 *            / \
 *           4   8
 *          /   / \
 *         11  13  4
 *        /  \    / \
 *       7    2  5   1
 *       
 *   Return
 *     [
 *          [5,4,11,2],
 *          [5,8,4,5]
 *     ]
 *
 */
public class path_sum_II {
    
    /**
     * Solution 1:
     *      using DFS algorithm
     *      
     * @param root
     * @param sum
     * @return the Linked-list those are satisfied.
     */
    public static List<List<Integer>> pathSum1(TreeNode root, int sum) {
        List<List<Integer>> result  = new LinkedList<List<Integer>>(); 
        List<Integer> currentResult  = new LinkedList<Integer>();
        
        pathSum(root,sum,currentResult,result);
        return result;
    }
    
    /**
     * implement a recursion function for DFS
     * 
     * @param root
     * @param sum
     * @param currentResult
     * @param result
     */
    public static void pathSum(TreeNode root, int sum, List<Integer> currentResult, List<List<Integer>> result) {
        if (root == null)  return;
        
        currentResult.add(new Integer(root.val));  // add current node value into the template result list
        if (root.left == null && root.right == null && sum == root.val) {  // satisfied leaf
            result.add(new LinkedList<Integer>(currentResult));  // add into the result list<list>
            currentResult.remove(currentResult.size() - 1);   //remove the temp one
            return;
        }
        else {  // recursion
            pathSum(root.left, sum - root.val, currentResult, result);
            pathSum(root.right, sum - root.val, currentResult, result);
        }
        currentResult.remove(currentResult.size() - 1);  // trace-back by one step
    }
    
    
    public static void main(String[] args) {
        Integer[] data = {5,4,8,11,null,13,4,7,2,null,null,null,null,5,1};
        BinTree bt = new BinTree();
        bt.bTreeRoot = bt.createTree(data, 0, 15);  //creating a binary tree.
        
        List<List<Integer>> ll = pathSum1(bt.bTreeRoot, 22);
        
        Iterator<List<Integer>> tt = ll.iterator();
        
        //printing the list
        while(tt.hasNext()) {
            Iterator<Integer> t = tt.next().iterator();
            while(t.hasNext()) {
                System.out.printf(t.next() + " ");
            }
            System.out.println();
        }
    }
}
