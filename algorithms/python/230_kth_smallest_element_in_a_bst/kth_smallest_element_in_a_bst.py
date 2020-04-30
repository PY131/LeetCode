# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
    You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example:
    Input: root = [5,3,6,2,4,null,null,1], k = 3
           5
          / \
         3   6
        / \
       2   4
      /
     1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""

import sys
sys.path.append("../")
from self_made_libs.binary_tree import BTreeHelper, TreeNode

class Solution(object):

    def kthSmallest(self, root, k):
        """
            on the base of v1, we can stop early as soon as we found the k-th item
            here we use iterative traversal
            now the space complexity reduce to O(1)
        """
        res = root.val   
        s = []
        p = root
        while k:
            while p:
                s.append(p)
                p = p.left
            p = s.pop()
            res = p.val
            p = p.right
            k -= 1

        return res

    def kthSmallest_v1(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        :idea: using in-order traversal, and the k-th item is the target
        :complexity: O(n) in time and O(n) in space
        """
        def help(root, res):
            if not root:
                return            
            help(root.left, res)
            res.append(root.val)
            help(root.right, res)

        arr = []
        help(root, arr)
        return arr[k-1]

if __name__ == '__main__':
    BT = BTreeHelper()
    S = Solution()
    arr = [5,3,6,2,4,None,None,1]
    root = BT.build_a_tree(arr)
    # BT.trav_pre(root)
    res = S.kthSmallest(root, 3)
    print res
