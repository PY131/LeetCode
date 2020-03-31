# coding: utf8
# python 2.7
"""
@Link: https://leetcode-cn.com/problems/delete-node-in-a-linked-list

@author: Pn

@Problem: Write a function to delete a node (except the tail) in a singly linked list, 
          given only access to that node.

@Example: Given linked list -- head = [4,5,1,9]
    Input: head = [4,5,1,9], node = 5
    Output: [4,1,9]
    Explanation: You are given the second node with value 5, 
                 the linked list should become 4 -> 1 -> 9 after calling your function.

@Note:
    The linked list will have at least two elements.
    All of the nodes' values will be unique.
    The given node will not be the tail and it will always be a valid node of the linked list.
    Do not return anything from your function.
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

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        :idea: assgin node to node.next and remove node.next
        :complexity: O(1)
        """
        # if not node.next:
        #     node = None
        # else:
        #     node.val = node.next.val
        #     node.next = node.next.next

        # as we know that node isn't the tail, so
        node.val = node.next.val
        node.next = node.next.next

# test code
if __name__ == '__main__':
    so = Solution()
    arr = [4,5,1,9]
    head = so.build_a_list(arr)
    so.display_a_list(head, prefix="before: ")
    tar = head.next
    new_head = so.deleteNode(tar)
    so.display_a_list(head, prefix="after:  ")
