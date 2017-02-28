import tree.BinTree;
//import tree.BinTree.TreeNode;

public class find_mode_in_binary_search_tree {
    
    public static class Solution1 {
        
        public int[] findMode(BinTree.TreeNode root) {
            inorder(root);
            modes = new int[modeCount];
            modeCount = 0;
            currCount = 0;
            inorder(root);
            return modes;
        }

        private int currVal;
        private int currCount = 0;
        private int maxCount = 0;
        private int modeCount = 0;
        
        private int[] modes;

        private void handleValue(int val) {
            if (val != currVal) {
                currVal = val;
                currCount = 0;
            }
            currCount++;
            if (currCount > maxCount) {
                maxCount = currCount;
                modeCount = 1;
            } else if (currCount == maxCount) {
                if (modes != null)
                    modes[modeCount] = currVal;
                modeCount++;
            }
        }
        
        private void inorder(BinTree.TreeNode root) {
            if (root == null) return;
            inorder(root.left);
            handleValue(root.val);
            inorder(root.right);
        }
    }
    
    public static void main(String[] args) {
        Integer data[] = {1,null,2,null,null,3};
        BinTree bt = new BinTree();
        
        bt.createBintree(data);
        bt.LevelOrder(bt.bTreeRoot);
        
        Solution1 s1 = new Solution1();
        int modes[] = s1.findMode(bt.bTreeRoot);
        
        for(int i: modes){
            System.out.println(i+"  ");
        }
                
        bt.deleteTree(bt.bTreeRoot);
    }
}
