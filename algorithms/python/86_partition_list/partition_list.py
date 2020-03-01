# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/partition-list/

Given a linked list and a value x, 
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:
    Input: head = 1->4->3->2->5->2, x = 3
    Output: 1->2->2->4->3->5
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

    def partition_v0(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        pivot = ListNode(-1)
        pivot.next = head
        pre = pivot
        p0 = pre
        p1 = p0.next
        unchanged = True
        while p1:
            if p1.val < x:
                if unchanged:
                    pre = p1
                    p0 = p1
                    p1 = p1.next
                else:
                    p0.next = p1.next
                    p1.next = pre.next
                    pre.next = p1
                    pre = p1
                    p1 = p0.next
            else:
                p0 = p1
                p1 = p0.next
                unchanged = False
        return pivot.next

    def partition_v1(self, head, x):
        """using two list pointer
        """
        pivot_0 = ListNode(-1)
        pivot_1 = ListNode(-1)
        p_0 = pivot_0
        p_1 = pivot_1
        p = head
        while p:
            if p.val < x:
                p_0.next = p
                p_0 = p  
            else:
                p_1.next = p
                p_1 = p
            p = p.next
        p_0.next = pivot_1.next
        p_1.next = None
        return pivot_0.next

if __name__ == "__main__":
    so = Solution()
    arr = [1,4,3,2,5,2]
    head = so.build_a_list(arr)
    so.display_a_list(head, prefix="before: ")

    new_head = so.partition_v1(head, 3)
    so.display_a_list(new_head, prefix="after:  ")

