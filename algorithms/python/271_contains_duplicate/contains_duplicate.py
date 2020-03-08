# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/contains-duplicate

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

Example 1:
    Input: [1,2,3,1]
    Output: true
Example 2:
    Input: [1,2,3,4]
    Output: false
Example 3:
    Input: [1,1,1,3,3,4,3,2,4,2]
    Output: true
"""

class Solution(object):

    def containsDuplicate(self, nums):
        """using hash map
        """
        M = {}
        for val in nums:
            if val in M:
                return True
            M[val] = 1
        return False

    def containsDuplicate_v3(self, nums):
        """base on method v2, add judgement with-in quick sort process
        """
        def judge_in_quick_sort(nums, lo, hi):
            if not lo < hi:
                return False
            pivot = nums[lo]
            i, j = lo, hi
            while i < j:
                while i < j and pivot < nums[j]:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= pivot:
                    if nums[i] == pivot:
                        return True
                    i += 1
                nums[j] = nums[i]
            nums[j] = pivot
            return False or judge_in_quick_sort(nums, lo, i - 1) or judge_in_quick_sort(nums, j + 1, hi)

        return judge_in_quick_sort(nums, 0, len(nums) - 1)

    def containsDuplicate_v2(self, nums):
        """
            naive force-brute may cost O(n^2) time complexity
            as we can use sort to reduce the complexity to O(nlogn)
        """
        # e.g. use quick sort
        def quick_sort(nums, lo, hi):
            if not lo < hi:
                return
            pivot = nums[lo]
            i, j = lo, hi
            while i < j:
                while i < j and pivot < nums[j]:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= pivot:
                    i += 1
                nums[j] = nums[i]
            nums[j] = pivot
            quick_sort(nums, lo, i - 1)
            quick_sort(nums, j + 1, hi)

        quick_sort(nums, 0, len(nums) - 1)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

    def containsDuplicate_v1(self, nums):
        """a little trick base on v0
        """
        return len(set(nums)) != len(nums)

    def containsDuplicate_v0(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        :method 1 force-brute
        """
        S = set()
        for val in nums:
            if val in S:
                return True
            S.add(val)
        return False

if __name__ == "__main__":
    so = Solution()
    arr = [1,1,1,3,3,4,3,2,4,2]
    arr = [1,2,3,4]
    # arr = [1,2,3,1]
    arr = [3,1,2,4,6,5]
    res = so.containsDuplicate(arr)
    print res
