# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p_long = p1 = pHead1
        p_short = p2 = pHead2
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
        if not p1:
            p1, p2 = p2, p1
            p_long, p_short = p_short, p_long
        while p1:
            p1 = p1.next
            p_long = p_long.next
        while p_long != p_short:
            p_long = p_long.next
            p_short = p_short.next
        return p_long

    def FindFirstCommonNode_v1(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            p1 = p1.next if p1 else pHead2
            p2 = p2.next if p2 else pHead1
        return p1