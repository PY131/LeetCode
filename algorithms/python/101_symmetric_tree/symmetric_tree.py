# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/symmetric-tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.
"""

import sys
sys.path.append("../")
from self_made_libs.binary_tree import BTreeHelper, TreeNode

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        :idea: rewrite v0 by iteratively
        :complexity: time: O(n), space: O(n)
        """
        Q = []
        Q.append(root)
        Q.append(root)
        while Q:
            l = Q.pop()
            r = Q.pop()
            if (not l) and (not r):
                continue
            elif (not l) or (not r) or (l.val != r.val):
                return False
            Q.append(l.left)
            Q.append(r.right)
            Q.append(l.right)
            Q.append(r.left)
        return True

    def isSymmetric_v0(self, root):
        def mirror(node_1, node_2):
            if not node_1 and not node_2:
                return True
            elif not node_1 or not node_2:
                return False
            return node_1.val == node_2.val \
                   and mirror(node_1.left, node_2.right) \
                   and mirror(node_1.right, node_2.left)

        return mirror(root, root)

# test code
if __name__ == '__main__':
    BT = BTreeHelper()
    S = Solution()
    arr = [1,2,2,3,4,4,3]
    arr = [1,2,2,None,3,None,3]
    root = BT.build_a_tree(arr)
    res = S.isSymmetric(root)
    print res
