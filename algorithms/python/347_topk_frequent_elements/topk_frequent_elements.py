# coding: utf8
# python 2.7
"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Note:
    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
    It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
    You can return the answer in any order.
"""
from Queue import PriorityQueue

class Solution(object):

    # limited_size-min_heap(
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        :idea: 
         - using a map to count - O(n)
         - using a PQ to get the topK - O(nlogk)
        """
        res = []

        # counting
        num2cnt = {}
        for x in nums:
            if x in num2cnt:
                num2cnt[x] += 1
            else:
                num2cnt[x] = 1
        # topk
        pq = PriorityQueue()
        for x, cnt in num2cnt.iteritems():
            if pq.qsize() < k:
                pq.put((cnt, x))
                continue
            top = pq.get()
            if cnt > top[0]:
                top = (cnt, x)
            pq.put(top)
        
        # return
        while k:
            cnt, x = pq.get()
            res.append(x)
            k -= 1
        return res

if __name__ == '__main__':
    so = Solution()
    nums = [4,1,-1,2,-1,2,3]
    k = 2
    res = so.topKFrequent(nums, k)
    print res
