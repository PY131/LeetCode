# coding: utf8
# python 2.7
"""
Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
    Input: [3,2,1,5,6,4] and k = 2
    Output: 5
Example 2:
    Input: [3,2,3,1,2,4,5,5,6] and k = 4
    Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

Link: https://leetcode-cn.com/problems/kth-largest-element-in-an-array
"""
import sys
sys.path.insert(0, "../")
from self_made_libs.priority_queue import PriorityQueueNew
from Queue import PriorityQueue

#-------------- short cut --------------#

class PriorityQueueNew_V2(object):

    def __init__(self, arr=[], max_limit=0):
        self.size = max_limit
        self.H = arr[:max_limit]
        for i in range(self.size / 2 - 1, -1, -1):  # 建堆, 从第一个非叶子节点往上
            self._adjust(i)
        for val in arr[max_limit:]:
            if val > self.H[0]:
                self.H[0] = val
                self._adjust(0)

    def _adjust(self, i):
        while i < self.size:
            k = l = 2*i+1
            r = l+1
            if r < self.size and self.H[r] < self.H[l]:
                k = r
            if k < self.size and self.H[k] < self.H[i]:
                self.H[k], self.H[i] = self.H[i], self.H[k]
            i = k

    def top(self):
        return self.H[0]

class Solution_2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # idea 1: sorted it the find - O(nlogn)
        # idea 2: using a min-heap with limited-size k - O(nlogk) - try this here
        pq = PriorityQueueNew_V2(nums, max_limit=k)
        return pq.top()

#-------------- original version --------------#

class Solution(object):

    def findKthLargest(self, nums, k):
        # using python lib
        pq = PriorityQueue()
        for i, x in enumerate(nums):
            if i < k:
                pq.put((x, x))
                continue
            top = pq.get(block=False)
            if x > top[0]:
                top = (x, x)
            pq.put(top)
        return pq.get()[0]

    def findKthLargest_v1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # idea 1: sorted it the find - O(nlogn)
        # idea 2: using a min-heap with limited-size k - O(nlogk) - try this here
        pq = PriorityQueueNew()
        for i, x in enumerate(nums):
            if i < k:
                pq.put((x, x))
                continue
            if x > pq.top()[0]:
                pq.pop()
                pq.put((x, x))
        return pq.top()[0]

if __name__ == '__main__':
    so = Solution_2()
    nums = [3,2,1,5,6,4]
    k = 2
    res = so.findKthLargest(nums, k)
    print res
