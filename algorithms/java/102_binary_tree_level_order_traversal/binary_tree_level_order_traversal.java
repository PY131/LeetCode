import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import tree.BinTree;
import tree.BinTree.TreeNode;

public class binary_tree_level_order_traversal {
    
    /**
     * Solution 1:
     *      using recursive method
     * @param root
     * @return
     */
    public static List<List<Integer>> levelOrder_1(TreeNode root) {
        // note: here we should use ArrayList instead of LinkedList to get a fast speed
        List<List<Integer>> res  = new ArrayList<List<Integer>>(); 
        
        CurrentlevelOrder(root, res, 0);
        return res;
    }
    
    /**
     * recursion for traversal
     * @param root
     * @param res is the List<List<Integer>> of result
     * @param depth of the tree.
     */
    private static void CurrentlevelOrder(TreeNode root, List<List<Integer>> res, int depth) {
        if(root == null)  return;   
        
        if(res.size() == depth)  res.add(new ArrayList<Integer>());

        List<Integer> current_res = res.get(depth);
        current_res.add(root.val);
        
        CurrentlevelOrder(root.left, res, depth + 1);
        CurrentlevelOrder(root.right, res, depth + 1);
    }

    
    // test code
    public static void main(String[] args) {
        // create a binary tree
        Integer[] data = {5,4,6,11,null,13,4,7,2,null,null,null,null,null,1};
        BinTree bt = new BinTree();
        bt.bTreeRoot = bt.createTree(data, 0, 15);
        
        List<List<Integer>> ll = levelOrder_1(bt.bTreeRoot);
        
        // printing the list
        Iterator<List<Integer>> tt = ll.iterator();
        while(tt.hasNext()) {
            Iterator<Integer> t = tt.next().iterator();
            while(t.hasNext()) {
                System.out.printf(t.next() + " ");
            }
            System.out.println();
        }
    }

}
