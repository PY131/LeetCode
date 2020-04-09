# coding: utf8
# python 2.7
"""
link: https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

import sys
sys.path.append("../")
from self_made_libs.binary_tree import BTreeHelper, TreeNode

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        s = [root]
        while s:
            q = []
            p = []
            for n in s:
                if n:
                    q.append(n.val)
                    p.extend([n.left, n.right])
            if q:
                res.append(q)
            else:
                break
            s = p
        return res

# test code
if __name__ == '__main__':
    BT = BTreeHelper()
    S = Solution()
    arr = [3,9,20,None,None,15,7]
    root = BT.build_a_tree(arr)
    res = S.levelOrder(root)
    print res
