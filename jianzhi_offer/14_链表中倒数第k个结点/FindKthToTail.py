# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        p1 = p2 = head
        try:
            t = 0
            while t < k:
                p1 = p1.next
                t += 1
            while p1:
                p1 = p1.next
                p2 = p2.next
        except:
            return None
        return p2