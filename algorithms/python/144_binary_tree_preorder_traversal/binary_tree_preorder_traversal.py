# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/binary-tree-preorder-traversal
Given a binary tree, return the preorder traversal of its nodes' values.

Example:
    Input: [1,null,2,3]
       1
        \
         2
        /
       3
    Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
import sys
sys.path.append("../")
from self_made_libs.binary_tree import BTreeHelper, TreeNode

class Solution(object):

    def preorderTraversal_v1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        :idea: do it iteratively, complexity: time O(n) space O(n)
        """
        res = []
        S = [root] if root else []
        while S:
            p = S.pop()
            res.append(p.val)
            if p.right:
                S.append(p.right)
            if p.left:
                S.append(p.left)
        return res

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        :idea: do it recursively
        """
        res = []
        if not root:
            return res
        res.append(root.val)
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))
        return res

if __name__ == '__main__':
    BT = BTreeHelper()
    S = Solution()
    arr = [1,2,2,None,3,None,3]
    root = BT.build_a_tree(arr)
    res = S.preorderTraversal_v1(root)
    print res
