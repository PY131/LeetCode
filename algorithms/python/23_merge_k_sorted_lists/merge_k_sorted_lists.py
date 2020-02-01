# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/merge-k-sorted-lists

Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.

Example:
    Input:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    Output: 1->1->2->3->4->4->5->6
"""

from Queue import PriorityQueue

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class PriorityQueue_v2(object):
    '''implement of PriorityQueue using min-heap
        each node format as [k, v] while k is priority
    '''
    def __init__(self, kv_arr = []):
        self.kv_arr = kv_arr
        self.size = len(kv_arr)
        self.build_heap()

    def queue(self):
        return self.kv_arr

    def build_heap(self):
        for i in range(self.size / 2 - 1, - 1, -1):
            self._adjust(i)

    def _swap(self, i, j):
        self.kv_arr[i], self.kv_arr[j] = \
        self.kv_arr[j], self.kv_arr[i]

    def _adjust(self, i):
        '''down-ward adjust from i-th node in array list
        '''
        while i < self.size:
            lc = 2 * i + 1  # left child
            rc = 2 * i + 2  # right child
            kc = lc  # smaller child
            if rc < self.size and self.kv_arr[rc][0] < self.kv_arr[lc][0]:
                kc = rc
            if kc < self.size and self.kv_arr[kc][0] < self.kv_arr[i][0]:
                self._swap(i, kc)
            i = kc

    def put(self, kv):
        '''add a node'''
        self.kv_arr.append(kv)
        i = self.size
        self.size += 1
        while i > 0:
            p = (i - 1) / 2  # parent
            print i, p, self.kv_arr[i][0], self.kv_arr[p][0]
            if self.kv_arr[i][0] < self.kv_arr[p][0]:
                self._swap(i, p)
            i = p

    def get(self):
        '''get and pop a node'''
        self._swap(0, self.size - 1)
        res = self.kv_arr.pop()
        self.size -= 1
        self._adjust(0)
        return res

    def empty(self):
        return self.size == 0

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
        while p:
            print prefix, 
            print p.val,
            print "->" if p.next else "",
            p = p.next
        print ""

    def mergeKLists_v2(self, lists):
        """
        :method2: using a priority heap after one epoch in method 1
        :complexity: time: O(n * logm) - logm is the complexity of queue-heap
        :using PriorityQueue of python lib
        """
        p = pivot = ListNode(-1)
        # pq = PriorityQueue()
        pq = PriorityQueue_v2()
        for l in lists:
            if l:
                pq.put((l.val, l))
        while not pq.empty():
            _, l_min = pq.get()
            p.next = l_min
            p = p.next
            l_min = l_min.next
            if l_min:
                pq.put((l_min.val, l_min))
        return pivot.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        :method:
            1-st: find the minimal in head nodes
            2-nd: get the current minimal and let current list head move to next
        :complexity: time: O(n * m)
        """
        p = pivot = ListNode(-1)
        while lists:
            idx_min = -1
            for idx in range(len(lists)):
                l = lists[idx]
                if l and (idx_min < 0 or l.val < lists[idx_min].val):
                    idx_min = idx
            if idx_min < 0:
                break
            p.next = lists[idx_min]
            p = p.next
            lists[idx_min] = lists[idx_min].next
        return pivot.next

if __name__ == "__main__":
    so = Solution()
    arrs = [
        [1,4,5],
        [1,3,4],
        [2,6],
    ]
    # arrs = [
    #     [1],
    #     [0]
    # ]
    ls = []
    for arr in arrs:
        l = so.build_a_list(arr)
        so.display_a_list(l)
        ls.append(l)
    merged_l = so.mergeKLists_v2(ls)
    so.display_a_list(merged_l)
