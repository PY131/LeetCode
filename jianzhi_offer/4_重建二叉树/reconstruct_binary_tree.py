# coding: utf8
# python 2.7

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin or len(pre) != len(tin):
            return None
        root_val = pre[0]
        root_idx = tin.index(root_val)
        root = TreeNode(root_val)
        if root_idx > 0:
            root.left = self.reConstructBinaryTree(pre[1: root_idx+1], tin[0: root_idx])
        if root_idx < len(tin) - 1:
            root.right = self.reConstructBinaryTree(pre[root_idx+1: len(pre)], tin[root_idx+1: len(tin)])
        return root