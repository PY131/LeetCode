# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        
        def recursion(p1, p2):
            if not p2:
                return True
            if not p1 or p1.val != p2.val:
                return False
            return recursion(p1.left, p2.left) and recursion(p1.right, p2.right)
            
        return recursion(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)