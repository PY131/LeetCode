# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path 
    from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
import sys
sys.path.append("../")
from self_made_libs.binary_tree import BTreeHelper, TreeNode

class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        :idea: for current node, choose the max depth between left & right sub-tree,
               do it recursively - DFS
        :complexity: O(n): space, O(logn) consider the recursion depth
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# test code
if __name__ == '__main__':
    BT = BTreeHelper()
    S = Solution()
    arr = [3,9,20,None,None,15,7]
    root = BT.build_a_tree(arr)
    res = S.maxDepth(root)
    print res
