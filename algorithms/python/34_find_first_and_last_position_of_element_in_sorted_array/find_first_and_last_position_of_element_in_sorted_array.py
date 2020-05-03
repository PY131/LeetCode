# coding: utf8
# python 2.7
"""
@author: Pn
@problem_info:    
    Given an array of integers nums sorted in ascending order, 
    find the starting and ending position of a given target value.
    Your algorithm's runtime complexity must be in the order of O(log n).
    If the target is not found in the array, return [-1, -1].

@Here are some examples. 
    Example 1:
        Input: nums = [5,7,7,8,8,10], target = 8
        Output: [3,4]
    Example 2:
        Input: nums = [5,7,7,8,8,10], target = 6
        Output: [-1,-1]

@Link:
    https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # we can use binary-search, to find the first index of num >= target
        # 1-st idx1 --> num >= target
        # 2-nd idx2 --> num >= target + 1
        # if idx1 == idx2, means target does not exists, otherwise the range = [idx1, idx2-1]
        # complexity: time: O(log n)
        def index(nums, target):
            lo = 0
            hi = len(nums)
            while lo < hi:
                mi = lo + (hi - lo) / 2
                if nums[mi] < target:
                    lo = mi + 1
                else:
                    hi = mi
            return lo

        idx1 = index(nums, target)
        idx2 = index(nums, target + 1)
        return [idx1, idx2 - 1] if idx1 != idx2 else [-1, -1] 

if __name__ == '__main__':
    so = Solution()
    nums = [5,7,7,8,8,10]
    target = 6
    res = so.searchRange(nums, target)
    print res
    
