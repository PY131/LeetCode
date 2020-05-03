# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/find-peak-element

A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:
    Input: nums = [1,2,1,3,5,6,4]
    Output: 1 or 5 
    Explanation: Your function can return either index number 1 where the peak element is 2, 
                 or index number 5 where the peak element is 6.

Note:
Your solution should be in logarithmic complexity.
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # as we know that nums[i] ≠ nums[i+1]
        # then...O(logn)
        hi = len(nums) - 1
        lo = 0
        while lo < hi:
            mi = lo + (hi - lo) / 2
            if nums[mi] < nums[mi+1]:
                lo = mi + 1
            if mi + 1 > hi or nums[mi] > nums[mi+1]:
                hi = mi
        return lo

if __name__ == '__main__':
    so = Solution()
    nums = [1,2]
    res = so.findPeakElement(nums)
    print res


