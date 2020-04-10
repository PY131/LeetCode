# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/merge-sorted-array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
    Example:

Input:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3
Output: 
    [1,2,2,3,5,6]
"""


class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :idea: in fact, full nums1 from tail, we can avoid build a temporary list
        :complexity: time: O(n), space: O(1)
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while not i < 0 and not j < 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        if not j < 0:
            nums1[:j+1] = nums2[:j+1]

    def merge_v2(self, nums1, m, nums2, n):
        """
        :idea: using a new array to avoid the moving after each insert in method v1
        :complexity: time: O(n), space: O(n)
        """
        S = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                S.append(nums1[i])
                i += 1
            else:
                S.append(nums2[j])
                j += 1
        while i < m:
            S.append(nums1[i])
            i += 1
        while j < n:
            S.append(nums2[j])
            j += 1
        nums1[:m+n] = S

    def merge_v1(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        :idea: force brute: compare one-by-one, once n2 > n1, move n1 for insert n2
        :complexity: time: O(n^2)
        """
        i = 0
        j = 0
        while i < m + n and j < n:
            if nums2[j] < nums1[i]:
                nums1[i+1: m+j+1] = nums1[i: m+j]
                nums1[i] = nums2[j]
                j += 1
            else:
                i += 1
        if j < n:
            nums1[m+j:] = nums2[j:]


if __name__ == "__main__":
    so = Solution()
    nums1 = [2,5,6,0,0,0]
    nums2 = [1,2,3]
    m = 3
    n = 3
    so.merge(nums1, m, nums2, n)
    print nums1
