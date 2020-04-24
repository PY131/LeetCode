# coding: utf8
# python 2.7
"""
Write a program to find the node at which the intersection of two singly linked lists begins.
Example 1:
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
    Output: Reference of the node with value = 8
    Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
Note:
    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.

Link: https://leetcode-cn.com/problems/intersection-of-two-linked-lists
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

    def build_requre_list(self, arr1, arr2, idx=0):
        head1 = self.build_a_list(arr1)
        head2 = self.build_a_list(arr2)
        p1 = head1
        while idx:
            p1 = p1.next
            idx -= 1        
        p2 = head2
        while p2.next:
            p2 = p2.next
        p2.next = p1
        return head1, head2

    def display_a_list(self, head, prefix = ""):
        p = head
        print prefix, 
        while p:
            print p.val,
            print "->" if p.next else "",
            p = p.next
        print ""

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        :complexity: time: O(n), space: O(1)
        :idea: using some pointers
        """
        a1 = a2 = headA
        b1 = b2 = headB
        while a1 and b1:
            a1 = a1.next
            b1 = b1.next
        if not b1:
            b1 = a1
            a2, b2 = b2, a2
        while b1:
            b1 = b1.next
            b2 = b2.next
        while a2 and b2:
            if a2 == b2:
                return a2
            a2 = a2.next
            b2 = b2.next
        return None

    def getIntersectionNode_v1(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        :complexity: time: O(n), space: O(n)
        :idea: using a Map to record
        """
        M = {}
        p1 = headA
        p2 = headB
        while p1 not in M and p2 not in M:
            M[p1] = 'a'
            M[p2] = 'b'
            p1 = p1.next
            p2 = p2.next
        return p1 if p1 in M else p2

if __name__ == "__main__":

    so = Solution()
    arr1 = [4,1,8,4,5]
    arr2 = [5,0,1]
    head1, head2 = so.build_requre_list(arr1, arr2, idx=2)
    so.display_a_list(head1, prefix="list 1: ")
    so.display_a_list(head2, prefix="list 1: ")

    inter = so.getIntersectionNode(head1, head2)
    so.display_a_list(inter, prefix="from intersection:  ")
