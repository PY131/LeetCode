# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/odd-even-linked-list

Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
    Input: 1->2->3->4->5->NULL
    Output: 1->3->5->2->4->NULL
Example 2:
    Input: 2->1->3->5->6->4->7->NULL
    Output: 2->3->6->7->1->5->4->NULL

Note:
    The relative order inside both the even and odd groups should remain as it was in the input.
    The first node is considered odd, the second node even and so on ...
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

    def oddEvenList_v1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def help(h):
            # assert h not None
            if (not h.next) or (not h.next.next):
                return h, h
            p0, p1 = help(h.next.next)
            h.next.next = p1.next
            p1.next = h.next
            h.next = p0
            return h, p1

        return head if not head else help(head)[0]

    def oddEvenList_v2(self, head):
        '''iteratively
        '''
        last_0 = head
        head_1 = head.next if head else None
        last_1 = head_1
        new_0 = last_1.next if last_1 else None
        new_1 = new_0.next if new_0 else None
        while new_0:
            new_0.next = head_1
            last_0.next = new_0
            last_1.next = new_1
            last_0 = new_0
            last_1 = new_1
            new_0 = last_1.next if last_1 else None
            new_1 = new_0.next if new_0 else None
        return head

    def oddEvenList_v3(self, head):
        '''iteratively method 2
        '''
        if not head: return head
        P1 = p1 = head
        P2 = p2 = head.next
        while p2 and p2.next:
            p1.next = p2.next
            p1 = p1.next
            p2.next = p1.next
            p2 = p2.next
        p1.next = P2
        return P1

if __name__ == "__main__":

    so = Solution()
    arr = [1,2,3,4,5]
    head = so.build_a_list(arr)
    so.display_a_list(head, prefix="before: ")

    new_head = so.oddEvenList_v3(head)

    so.display_a_list(new_head, prefix="after:  ")
