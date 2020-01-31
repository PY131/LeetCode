# coding: utf8
# python 2.7
"""
Given a linked list, 
remove the n-th node from the end of list and return its head.

Example:
    Given linked list: 1->2->3->4->5, and n = 2.
    After removing the second node from the end, 
    the linked list becomes 1->2->3->5.

Note: Given n will always be valid.
Follow up: Could you do this in one pass?

link: https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
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

    def display_a_list(self, head):
        p = head
        while p:
            print p.val,
            print "->" if p.next else "",
            p = p.next
        print ""

    def removeNthFromEnd(self, head, n):
        '''
            double traversing pointer, 
            one is falling behind anther by n-steps
        '''
        pivot = ListNode(-1)
        pivot.next = head
        p1 = p2 = pivot
        lag = 0
        while p2.next:
            if lag < n:
                lag += 1
            else:
                p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return pivot.next

if __name__ == "__main__":
    so = Solution()
    arr = [1]
    head = so.build_a_list(arr)
    n = 1
    so.display_a_list(head)
    head = so.removeNthFromEnd(head, n)
    so.display_a_list(head)
