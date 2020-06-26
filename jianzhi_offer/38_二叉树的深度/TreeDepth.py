# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        def help(root):
            # return depth and check result
            if not root:
                return 0, True
            d_l, flag_l = help(root.left)
            d_r, flag_r = help(root.right)
            return 1 + max(d_l, d_r), abs(d_l - d_r) <= 1

        return help(pRoot)[1]