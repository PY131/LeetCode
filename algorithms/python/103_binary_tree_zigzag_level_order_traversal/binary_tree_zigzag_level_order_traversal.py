# coding: utf8
# python 2.7
"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
    (ie, from left to right, then right to left for the next level and alternate between).

For example:
    Given binary tree [3,9,20,null,null,15,7],
         3
        / \
       9  20
         /  \
        15   7
    return its zigzag level order traversal as:
    [
        [3],
        [20,9],
        [15,7]
    ]
Link: https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
"""

import sys
sys.path.append("../")
from self_made_libs.binary_tree import BTreeHelper, TreeNode

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        :based on level traversal, using a flag for zig-zag
        :complexity: time O(n), space O(n) as we need return res
        """
        res = []
        s = [root]
        zigzag = True
        while s:
            sub_res = []
            new_s = []
            for p in s:
                if p:
                    if zigzag:
                        sub_res.append(p.val)
                    else:
                        sub_res.insert(0, p.val)
                    new_s.extend([p.left, p.right])
            if not sub_res:
                break
            res.append(sub_res)
            s = new_s
            zigzag = not zigzag
        return res

# test code
if __name__ == '__main__':
    BT = BTreeHelper()
    S = Solution()
    arr = [3,9,20,None,None,15,7]
    root = BT.build_a_tree(arr)
    res = S.zigzagLevelOrder(root)
    print res
