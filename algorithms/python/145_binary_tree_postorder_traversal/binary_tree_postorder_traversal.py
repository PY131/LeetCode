# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/binary-tree-postorder-traversal
Given a binary tree, return the postorder traversal of its nodes' values.

Example:
    Input: [1,null,2,3]
       1
        \
         2
        /
       3
    Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
import sys
sys.path.append("../")
from self_made_libs.binary_tree import BTreeHelper, TreeNode

class Solution(object):

    def postorderTraversal_v1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        :idea: do it iteratively, complexity: time O(n) space O(n)
        :      just reverse the output of root->right->left
        """
        res = []
        S = [root] if root else []
        while S:
            p = S.pop()
            res.insert(0, p.val)
            if p.left:
                S.append(p.left)
            if p.right:
                S.append(p.right)
        return res

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        :idea: do it recursively
        """
        res = []
        if not root:
            return res
        res.extend(self.postorderTraversal(root.left))
        res.extend(self.postorderTraversal(root.right))
        res.append(root.val)
        return res

if __name__ == '__main__':
    BT = BTreeHelper()
    S = Solution()
    arr = [1,2,2,None,3,None,3]
    root = BT.build_a_tree(arr)
    res = S.postorderTraversal_v1(root)
    print res
