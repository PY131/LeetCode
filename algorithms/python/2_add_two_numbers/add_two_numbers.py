# coding: utf8
# python 2.7
"""
- Problem:
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order and each of their nodes contain a single digit. 
    Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

- Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Singly_Linked_List(object):

    def __init__(self, nums):
        # 用一个list来顺序初始单链表
        # assert nums is not empty
        self.head = None
        if nums:
            self.head = ListNode(nums[0])
            v = self.head
            for i in range(1, len(nums)):
                new_node = ListNode(nums[i])
                v.next = new_node
                v = new_node

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        p1 = l1
        p2 = l2
        flag = 0
        p3 = pivot = ListNode(-1)
        while p1 or p2 or flag:
            new_val = flag
            if p1:
                new_val += p1.val
                p1 = p1.next
            if p2:
                new_val += p2.val
                p2 = p2.next               
            flag = new_val / 10
            p3.next = ListNode(new_val % 10)
            p3 = p3.next
            if not p1 and not p2 and not flag:
                break
        return pivot.next

    def addTwoNumbers_1(self, l1, l2):
        '''模拟加法进位,加到l3上
        '''
        v1 = l1
        v2 = l2
        carry = 0
        # 初始化头节点
        l3 = None
        su = 0
        if v1 and v2:
            su = v1.val + v2.val
            v1 = v1.next
            v2 = v2.next
        elif v1:
            su = v1.val
            v1 = v1.next
        elif v2:
            su = v2.val
            v2 = v2.next
        else:
            return l3
        l3 = ListNode(su % 10)
        carry = su / 10
        v3 = l3
        while v1 or v2:
            su = carry
            if v1:
                su += v1.val
                v1 = v1.next
            if v2:
                su += v2.val
                v2 = v2.next
            carry = su / 10
            new_node = ListNode(su % 10)
            v3.next = new_node
            v3 = new_node
        if carry != 0:
            new_node = ListNode(carry)
            v3.next = new_node
        return l3

    def addTwoNumbers_2(self, l1, l2):
        '''写简介一些
        '''
        v1 = l1
        v2 = l2
        carry = 0
        # 初始化头节点
        l3 = ListNode(0)
        v3 = l3
        while v1 or v2:
            su = carry
            if v1:
                su += v1.val
                v1 = v1.next
            if v2:
                su += v2.val
                v2 = v2.next
            carry = su / 10
            new_node = ListNode(su % 10)
            v3.next = new_node
            v3 = new_node
        if carry != 0:
            new_node = ListNode(carry)
            v3.next = new_node
        return l3.next

if __name__ == "__main__":
    a = [1,5]
    b = [0]
    l1 = Singly_Linked_List(a)
    l2 = Singly_Linked_List(b)
    
    s = Solution()
    res = s.addTwoNumbers(l1.head, l2.head)
    while res:
        print res.val
        res = res.next
