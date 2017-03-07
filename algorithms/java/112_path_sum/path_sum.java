
import tree.BinTree;
import tree.BinTree.TreeNode;;

/**
 * @author Peng
 * 
 * Problem:
 *      Given a binary tree and a sum, 
 *      determine if the tree has a root-to-leaf path 
 *      such that adding up all the values along the path equals the given sum.
 */
public class path_sum {

    /**
     * using recursion
     * @param root
     * @param sum
     * @return true 
     */
    public static boolean hasPathSum1(TreeNode root, int sum) {
        if(root == null) return false; 
        if(root.left == null && root.right == null && sum == root.val)  return true;
        return hasPathSum1(root.left, sum - root.val) || hasPathSum1(root.right, sum - root.val);
    }
    
    public static void main(String[] args) {
        Integer[] data = {5,4,6,11,null,13,4,7,2,null,null,null,null,null,1};
        BinTree bt = new BinTree();
        bt.bTreeRoot = bt.createTree(data, 0, 15);
        
        int sum = 21;
        System.out.print(hasPathSum1(bt.bTreeRoot, sum));
    }

}
