# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        # using a map to record the mapping of list 1's node to 2's
        M = {None: None}
        p1 = pHead
        p2 = pivot = RandomListNode(-1)
        while p1:
            node = RandomListNode(p1.label)
            p2.next = node
            p2 = p2.next
            M[p1] = p2
            p1 = p1.next
        p1 = pHead
        p2 = pivot.next
        while p1:
            p2.random = M[p1.random]
            p1 = p1.next
            p2 = p2.next
        return pivot.next

    def Clone_v1(self, pHead):
        if not pHead:
            return None
        p1 = pHead
        while p1:
            p2 = RandomListNode(p1.label)
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
        p1 = pHead
        while p1:
            if p1.random:
                p1.next.random = p1.random.next
            p1 = p1.next.next
        p1 = pHead
        p2 = pHead_copy = p1.next
        while p1:
            p1.next = p2.next
            p1 = p1.next
            if p1:
                p2.next = p1.next
                p2 = p2.next
        return pHead_copy