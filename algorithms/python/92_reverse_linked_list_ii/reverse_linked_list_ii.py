# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/reverse-linked-list-ii

Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
    Input: 1->2->3->4->5->NULL, m = 2, n = 4
    Output: 1->4->3->2->5->NULL
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

    def reverseFirstN(self, head, n):
        pre = None
        cur = head
        i = 1
        while cur and i <= n:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
            i += 1
        if cur:
            head.next = cur
        return pre

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        :reverse of an linked list' nodes between m->n
        """
        pivot = ListNode(0)
        pivot.next = head
        pre = pivot
        cur = head
        i = 1
        while i < m:
            pre = cur
            cur = cur.next
            i += 1
        pre.next = self.reverseFirstN(cur, n - m + 1)
        return pivot.next

if __name__ == "__main__":
    so = Solution()
    arr = [3,5]
    head = so.build_a_list(arr)
    so.display_a_list(head, prefix="before: ")

    # new_head = so.reverseFirstN(head, n=3)
    # so.display_a_list(new_head, prefix="after:  ")

    new_head = so.reverseBetween(head, m=1, n=2)
    so.display_a_list(new_head, prefix="after:  ")

