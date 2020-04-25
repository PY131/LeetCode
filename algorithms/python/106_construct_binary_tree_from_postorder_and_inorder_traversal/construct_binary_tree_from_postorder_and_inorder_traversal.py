# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/construct-binary-tree-from-postorder-and-inorder-traversal/

Given postorder and inorder traversal of a tree, construct the binary tree.
Note:
    You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
"""

import sys
sys.path.append("../")
from self_made_libs.binary_tree import BTreeHelper, TreeNode

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        r_val = postorder[-1]
        r_idx = inorder.index(r_val)
        root = TreeNode(r_val)
        root.left = self.buildTree(inorder[:r_idx], postorder[:r_idx])
        root.right = self.buildTree(inorder[r_idx+1:], postorder[r_idx:-1])
        return root

if __name__ == '__main__':
    BT = BTreeHelper()
    S = Solution()
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    root = S.buildTree(inorder, postorder)
    BT.trav_pre(root)
