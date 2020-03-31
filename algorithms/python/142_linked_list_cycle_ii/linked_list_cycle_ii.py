# coding: utf8
# python 2.7
"""
@Link: https://leetcode-cn.com/problems/linked-list-cycle-ii

@author: Pn

@Problem: Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

@Example: 
    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node

@Note:
    Could you do it in O(n) time and O(1) space?
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def build_a_cycle_list(self, arr, idx=-1):
        pivot = ListNode(-1)
        p = pivot
        for it in arr:
            new_node = ListNode(it)
            p.next = new_node
            p = new_node
        if not idx < 0:
            p_tar = pivot
            while not idx < 0:
                p_tar = p_tar.next
                idx -= 1
            p.next = p_tar
        return pivot.next

    def display_a_list(self, head, prefix = "", limit = 100):
        idx = 0
        p = head
        print prefix, 
        while p and idx < limit:
            print p.val,
            print "->" if p.next else "",
            p = p.next
            idx += 1
        print ""

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        :idea: suppose we have a, b, c three runner, a's speed = 2 while b & c's speed = 1
            1. a, b begin at the same time
            2. we can assert that a would catch up b from behind if there is cycle
            3. set the index of the node a meet b is M, and the M equels to cycle's circumference
            4. after a, b meet each other, b, c go on continue
            5. next time b meet c would happen in cycle beginning node
        :complexity: time: O(n), space: O(1)
        """
        a = b = c = head
        has_meet = False
        while a and a.next:
            if has_meet:
                if b == c:
                    return b
                b = b.next
                c = c.next
            else:
                a = a.next.next
                b = b.next
                if a == b:
                    has_meet = True
        return None

    def detectCycle_1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        :idea: we can use a map to record the cycle's node, and iterative for the first repeat one
        :complexity: time: O(n), space: O(n)
        """
        M = {}
        p = head
        while p:
            if p in M:
                return p
            M[p] = 1
            p = p.next
        return None

# test code
if __name__ == '__main__':
    so = Solution()
    arr = [1,2]
    head = so.build_a_cycle_list(arr, 0)
    so.display_a_list(head, prefix="before: ", limit=10)
    res = so.detectCycle(head)
    print res.val
