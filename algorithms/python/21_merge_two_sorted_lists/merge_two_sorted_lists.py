# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/merge-two-sorted-lists

Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
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

    def mergeTwoLists(self, l1, l2):
        """iteritively
        """
        p3 = pivot = ListNode(-1)
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val < p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next
        if p1:
            p3.next = p1
        if p2:
            p3.next = p2
        return pivot.next            

    def mergeTwoLists_v2(self, l1, l2):
        """recursively
        """
        if (not l1) or (not l2):
            return l1 if l1 else l2
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists_v2(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists_v2(l1.next, l2)
            return l1

if __name__ == "__main__":
    so = Solution()
    arr1 = [1]
    arr2 = []
    l1 = so.build_a_list(arr1)
    l2 = so.build_a_list(arr2)
    so.display_a_list(l1)
    so.display_a_list(l2)
    l3 = so.mergeTwoLists(l1, l2)
    so.display_a_list(l3)
