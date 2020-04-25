# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/binary-tree-inorder-traversal
Given a binary tree, return the inorder traversal of its nodes' values.

Example:
    Input: [1,null,2,3]
       1
        \
         2
        /
       3
    Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
import sys
sys.path.append("../")
from self_made_libs.binary_tree import BTreeHelper, TreeNode

class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        :idea: do it iteratively, complexity: time O(n) space O(n)
        """
        def go_along_left(r, s):
            while r:
                s.append(r)
                r = r.left
        
        res = []
        S = []
        p = root
        while True:
            go_along_left(p, S)
            if not S:
                break
            p = S.pop()
            res.append(p.val)
            p = p.right
        return res

    def inorderTraversal_v1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        :idea: do it recursively
        """
        res = []
        if not root:
            return res
        res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res

# test code
if __name__ == '__main__':
    BT = BTreeHelper()
    S = Solution()
    arr = [1,2,2,None,3,None,3]
    root = BT.build_a_tree(arr)
    res = S.inorderTraversal(root)
    print res
