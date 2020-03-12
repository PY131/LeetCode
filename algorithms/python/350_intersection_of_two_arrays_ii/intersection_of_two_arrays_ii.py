# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/intersection-of-two-arrays-ii

Given two arrays, write a function to compute their intersection.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]

Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [4,9]

Note:
    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:
    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

class Solution(object):

    def intersection(self, nums1, nums2):
        """
        :idea: on the base of v3, we do not need extra memory res, just use one of given list to store the result
        """
        nums1.sort()
        nums2.sort()
        i, j, k = 0, 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1
        return nums1[:k]

    def intersection_v3(self, nums1, nums2):
        """
        :idea: sorted array, then compared one-by-one (using built-in sort)
        :complexity: time: O(nlogn), space: O(n)
        """
        nums1.sort()
        nums2.sort()
        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res

    def intersection_v2(self, nums1, nums2):
        """
        :idea: base on v1, map record the smaller list
        """
        res = []
        M = {}
        for  x in nums1 if len(nums1) < len(nums2) else nums2:
            if x in M:
                M[x] += 1
            else:
                M[x] = 1
        for x in nums2 if len(nums1) < len(nums2) else nums1:
            cnt = M.get(x, 0)
            if cnt > 0:
                res.append(x)
                M[x] -= 1
        return res

    def intersection_v1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        :idea: using a Map to record item in one list, and check one-by-one of another list
        :complexity: time: O(n), space: O(n)
        """
        res = []
        M = {}
        for  x in nums1:
            if x in M:
                M[x] += 1
            else:
                M[x] = 1
        for x in nums2:
            cnt = M.get(x, 0)
            if cnt > 0:
                res.append(x)
                M[x] -= 1
        return res

if __name__ == "__main__":
    so = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    res = so.intersection(nums1, nums2)
    print res
