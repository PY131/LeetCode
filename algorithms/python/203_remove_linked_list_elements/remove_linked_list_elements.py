# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/remove-linked-list-elements/

Remove all elements from a linked list of integers that have value val.

Example:
    Input:  1->2->6->3->4->5->6, val = 6
    Output: 1->2->3->4->5
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

    def removeElements_v1(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pivot = ListNode(0)
        pivot.next = head
        pre = pivot
        cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return pivot.next

    def removeElements(self, head, val):
        '''recursively
        '''
        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        return head if head.val != val else head.next

if __name__ == "__main__":

    so = Solution()
    arr = [1,2,6,3,6,5]
    head = so.build_a_list(arr)
    so.display_a_list(head, prefix="before: ")

    new_head = so.removeElements(head, 6)

    so.display_a_list(new_head, prefix="after:  ")
