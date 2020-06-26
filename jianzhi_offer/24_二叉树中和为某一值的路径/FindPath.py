# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:  # 空节点
            return []
        if not root.left and not root.right:  # 叶节点
            return [] if root.val != expectNumber else [[root.val]]
        l = self.FindPath(root.left, expectNumber - root.val)
        r = self.FindPath(root.right, expectNumber - root.val)
        return [[root.val] + x for x in l + r]