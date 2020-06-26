# coding: utf8
# python 2.7
"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
    Input: 4->2->1->3
    Output: 1->2->3->4
Example 2:
    Input: -1->5->3->4->0
    Output: -1->0->3->4->5

Link: https://leetcode-cn.com/problems/sort-list
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

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # idea1: using a PQ to store the val->node mapping, using O(nlogn) in time a O(n) in space
        from Queue import PriorityQueue
        Q = PriorityQueue()
        p = head
        pivot = ListNode(-1)
        while p:
            Q.put((p.val, p))
            p = p.next
        tmp = pivot
        while not Q.empty():
            _, p = Q.get()
            tmp.next = p
            tmp = p
        tmp.next = None
        return pivot.next

# test code
if __name__ == '__main__':
    S = Solution()
    arr = [4,2,1,3]
    head = S.build_a_list(arr)
    res = S.sortList(head)
    S.display_a_list(res)
