# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

    Input: 1->1->2
    Output: 1->2

    Input: 1->1->2->3->3
    Output: 1->2->3
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

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        next = cur.next if cur else None
        while next:
            if cur.val == next.val:
                cur.next = next.next
            else:
                cur = next
            next = next.next
        return head

    def deleteDuplicates_v1(self, head):
        '''recursively
        '''
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates_v1(head.next)
        if head.val == head.next.val:
            head = head.next
        return head

if __name__ == "__main__":
    so = Solution()
    arr = [1,2,2,3,3,5]
    head = so.build_a_list(arr)
    so.display_a_list(head, prefix="before: ")

    new_head = so.deleteDuplicates_v1(head)
    so.display_a_list(new_head, prefix="after:  ")

