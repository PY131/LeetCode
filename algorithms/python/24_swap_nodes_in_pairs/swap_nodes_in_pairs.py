# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/swap-nodes-in-pairs

Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
    Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def build_a_list(self, arr):
        pivot = ListNode(-1)
        p = pivot
        for it in arr:
            new_node = ListNode(it)
            p.next = new_node
            p = new_node
        return pivot.next

    def display_a_list(self, head, prefix = ""):
        p = head
        print prefix, 
        while p:
            print p.val,
            print "->" if p.next else "",
            p = p.next
        print ""

    def swapPairs_v2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        :method: using only 1 pointer and 1 tmp
        """
        pivot = ListNode(-1)
        pivot.next = head
        p0 = pivot
        while p0.next and p0.next.next:
            p1 = p0.next
            p0.next = p1.next
            p1.next = p1.next.next
            p0.next.next = p1
            p0 = p1
        return pivot.next

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        :method: using 3 pointers
        """
        pivot = ListNode(-1)
        pivot.next = head
        p0 = pivot
        p1 = head
        p2 = p1.next if p1 else None
        while p1 and p2:
            p0.next = p2
            p1.next = p2.next
            p2.next = p1
            p0 = p1
            p1 = p1.next
            p2 = p1.next if p1 else None
        return pivot.next

if __name__ == "__main__":
    so = Solution()
    arr = [1,2,3,4]
    head = so.build_a_list(arr)
    so.display_a_list(head, prefix="before: ")
    new_head = so.swapPairs_v2(head)
    so.display_a_list(new_head, prefix="after:  ")
