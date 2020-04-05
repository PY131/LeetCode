# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/validate-binary-search-tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

import sys
sys.path.append("../")
from self_made_libs.binary_tree import BTreeHelper, TreeNode

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        :idea: using in-order travesal to see if the value is strictly increasing
        :complexity: do it iteratively, time: O(n), space: O(n)
        """
        def go_along_left_branch(root, S):
            v = root
            while v:
                S.append(v)
                v = v.left

        v = root
        S = []
        pre_val = float("-inf")
        while True:
            go_along_left_branch(v, S)
            if not S:
                break
            v = S.pop()
            if not pre_val < v.val:
                return False
            pre_val = v.val
            v = v.right
        return True

# test code
if __name__ == '__main__':
    BT = BTreeHelper()
    S = Solution()
    arr = [5,1,4,None,None,3,6]
    arr = [1,1]
    root = BT.build_a_tree(arr)
    res = S.isValidBST(root)
    print res
