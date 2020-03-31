# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/linked-list-cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, 
we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

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
        # link the tail to 2-nd node
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

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        :idea
            (1) suppose we have a,b two pointer
            (2) a, b start at the same time, a's speed = 2, while b's speed = 1
            (3) we can assert that a can catch up b if there is cycle
            (4) step cost's is the cycle's perimeter circumference
        :complexity: O(n) in time, O(1) is space
        """
        a = head
        b = head
        while a and a.next:
            a = a.next.next
            b = b.next
            if a == b:
                return True
        return False

# test code
if __name__ == '__main__':
    so = Solution()
    arr = [3,2,0,-4]
    head = so.build_a_cycle_list(arr, -1)
    so.display_a_list(head, prefix="before: ", limit=10)
    res = so.hasCycle(head)
    print res
