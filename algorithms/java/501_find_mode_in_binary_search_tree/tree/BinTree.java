package tree;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class BinTree {
      
    public TreeNode bTreeRoot;
    private static List<TreeNode> nodeLIst = new ArrayList<TreeNode>();  
    
    //Definition for a binary tree node.
    public class TreeNode {
        public int val;
        public TreeNode left;
        public TreeNode right;
        public TreeNode(int x) { val = x;}
    }  
    
    /****************************************************
     * using data[] array to creating binary tree
     * parameter:
     *      data: number array for binary tree(null means no child)
     *          example: [1,-1,2,2]:
     *          BT:     1
     *                   \
     *                    2
     *                     \
     *      index: root layer counting
     *      n: total nodes number
     *****************************************************/
//    public void createTree(TreeNode pNode, Integer[] data, int index, int n){
//        if(index < n && data[index].intValue() != -1)  //数组中NULL表示该节点为空
//        {
//            pNode = new TreeNode(data[index].intValue());  //new mem space
//            createTree(pNode.left, data, 2 * index + 1, n);  //loop through the b_tree using layer index, form 0 on
//            createTree(pNode.right, data, 2 * index + 2, n);
//        }
//        return;
//    }
    
    /****************************************************
     * using data[] array to creating binary tree
     * parameter:
     *      data: number array for binary tree(data can be any integer value)
     *****************************************************/
    public void createBintree(Integer[] array) {  
        for (int i = 0; i < array.length; i++) {  
            if(array[i] == null)  nodeLIst.add(null);
            else nodeLIst.add(new TreeNode(array[i].intValue()));  
        }  
  
        if (nodeLIst.size() > 0) {  
            for (int y = 0; y < array.length / 2 - 1; y++) {  
                //leftChild  
                if (null != nodeLIst.get(2 * y + 1)) {  
                    nodeLIst.get(y).left = nodeLIst.get(2 * y + 1);  
                }  
                //rightChild  
                if (null != nodeLIst.get(2 * y + 2)) {  
                    nodeLIst.get(y).right = nodeLIst.get(2 * y + 2);  
                }  
            }  
            //最后一个父节点不一定有孩子  
            int lastParentIndex = array.length / 2 - 1;  
            //左孩子  
            nodeLIst.get(lastParentIndex).left = nodeLIst.get(lastParentIndex * 2 + 1);  
            //奇数时候有右孩子  
            if (array.length % 2 == 1) {  
                nodeLIst.get(lastParentIndex).right = nodeLIst.get(lastParentIndex * 2 + 2);  
            }  
        }  
        
        bTreeRoot = nodeLIst.get(0);  
    }  
    
    
    /***********************************
     * delete a BT 
     * @param root 
     *********************************/ 
    public void deleteTree(TreeNode root){  
        if(root!=null){  
            deleteTree(root.left);  
            deleteTree(root.right);  
            root=null;  
        }  
    } 
    
    /***********************************
     * 二叉树的层次遍历 
     * @param root 
     ***********************************/
    public void LevelOrder(TreeNode T){  
        Queue<TreeNode> q = new LinkedList<TreeNode>();//Queue是个接口，不能实例化，而LinkedList实现了Queue接口，所以可以把LinkedList当队列使用  
        if(T != null)   q.offer(T);  
        while(!q.isEmpty()){  
            TreeNode tempNode = q.element();  
            System.out.println(tempNode.val);  
            if(tempNode.left != null)   q.offer(tempNode.left);  
            if(tempNode.right != null)  q.offer(tempNode.right);  
            q.poll();  
        }
    }
}




