# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        def in_order(root, res):
            if not root:
                return
            in_order(root.left, res)
            res.append(root)
            in_order(root.right, res)
            
        if not pRootOfTree:
            return None
        nodes = []
        in_order(pRootOfTree, nodes)
        n = len(nodes)
        for i in range(n-1):
            nodes[i].right = nodes[i+1]
            nodes[i+1].left = nodes[i]
        nodes[-1].right = nodes[0]
        nodes[0].left = nodes[-1]
        return nodes[0]