# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/reverse-linked-list

Reverse a singly linked list.

Example:
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL

Follow up:
    A linked list can be reversed either iteratively or recursively. 
    Could you implement both?
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

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

if __name__ == "__main__":
    so = Solution()
    arr = [1,2,3,4,5]
    head = so.build_a_list(arr)
    so.display_a_list(head, prefix="before: ")
    new_head = so.reverseList(head)
    so.display_a_list(new_head, prefix="after:  ")
