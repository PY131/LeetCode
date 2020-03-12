# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/intersection-of-two-arrays

Given two arrays, write a function to compute their intersection.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]

Note:
    Each element in the result must be unique.
    The result can be in any order.
"""

class Solution(object):

    def merge(self, nums, lo, mi, hi, tmp):
        i = lo
        j = mi + 1
        k = lo
        while i <= mi and j <= hi:
            if nums[i] <= nums[j]:
                tmp[k] = nums[i]
                i += 1
            else:
                tmp[k] = nums[j]
                j += 1
            k += 1

        while i <= mi:
            tmp[k] = nums[i]
            i += 1
            k += 1

        while j <= hi:
            tmp[k] = nums[j]
            j += 1
            k += 1

        for idx in range(lo, hi + 1):
            nums[idx] = tmp[idx]

    def merge_sort(self, nums, lo, hi, tmp=[]):
        if lo < hi:
            mi = (lo + hi) / 2
            self.merge_sort(nums, lo, mi, tmp)
            self.merge_sort(nums, mi+1, hi, tmp)
            self.merge(nums, lo, mi, hi, tmp)

    def intersection(self, nums1, nums2):
        """
        :method 3: sort and iterative
        :complexity: time: O(nlogn), space: O(x)
        """
        # using merge_sort as example
        res = set()
        self.merge_sort(nums1, 0, len(nums1) - 1, [0 for _ in range(len(nums1))])
        self.merge_sort(nums2, 0, len(nums2) - 1, [0 for _ in range(len(nums2))])

        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            print i, j, nums1[i], nums2[j]
            if nums1[i] != nums2[j]:
                while nums1[i] < nums2[j]:
                    i += 1
                while nums1[i] > nums2[j]:
                    j += 1
            else:
                res.add(nums1[i])
                tmp = nums1[i]
                while i < len(nums1) and nums1[i] == tmp:
                    i += 1
                while i < len(nums2) and nums2[j] == tmp:
                    j += 1
        return list(res)

    def intersection_v2(self, nums1, nums2):
        """
        :method 2: using a map to record nums appear in first list, the check the second one
        :complexity: time: O(n) space: O(n)
        """
        res = set()
        M = {}
        for x in nums1:
            M[x] = 1
        for x in nums2:
            if x in M:
                res.add(x)
        return list(res)

    def intersection_v1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

if __name__ == "__main__":
    so = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4,11]
    res = so.intersection(nums1, nums2)
    print res
