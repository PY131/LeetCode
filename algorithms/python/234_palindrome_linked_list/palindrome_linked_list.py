# coding: utf8
# python 2.7
"""
@Link: https://leetcode-cn.com/problems/palindrome-linked-list

@author: Pn

@Problem: Given a singly linked list, determine if it is a palindrome.

@Example: 
    Example 1:
        Input: 1->2
        Output: false
    Example 2:
        Input: 1->2->2->1
        Output: true

@Note:
    Could you do it in O(n) time and O(1) space?
"""

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

    def isPalindrome(self, head):
        """
        :idea: 
        """

    def isPalindrome_v1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        :idea: use a list (simulate Stack & Queue) to help judging
        :complexity: time O(n), space: O(n)
        """
        S = []
        p = head
        while p:
            S.append(p.val)
            p = p.next
        for i in range(len(S)):
            if S[i] != S[-(i+1)]:
                return False
        return True

# test code
if __name__ == '__main__':
    so = Solution()
    arr = [1,2,2]
    head = so.build_a_list(arr)
    so.display_a_list(head, prefix="before: ")
    res = so.isPalindrome(head)
    print res
