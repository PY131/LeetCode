# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        res = []
        tmp = [root] if root else []
        while tmp:
            new_tmp = []
            for node in tmp:
                res.append(node.val)
                if node.left:
                    new_tmp.append(node.left)
                if node.right:
                    new_tmp.append(node.right)
            tmp = new_tmp
        return res