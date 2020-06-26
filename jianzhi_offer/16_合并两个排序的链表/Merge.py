# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2
        if not p1:
            return p2
        elif not p2:
            return p1
        if p1.val > p2.val:
            p1, p2 = p2, p1
        pivot = ListNode(-1)
        pivot.next = p1
        while p1.next:
            if p1.next.val <= p2.val:
                p1 = p1.next
            else:
                tmp = p1.next
                p1.next = p2
                p1, p2 = p2, tmp
        p1.next = p2
        return pivot.next