# coding: utf8
# python 2.7
"""
@author: Pn
@problem_info:    
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
    (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
    You are given a target value to search. If found in the array return its index, otherwise return -1.
    You may assume no duplicate exists in the array.
    Your algorithm's runtime complexity must be in the order of O(log n).

@examples. 
    Example 1:
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4
    Example 2:
        Input: nums = [4,5,6,7,0,1,2], target = 3
        Output: -1

@Link: https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # time: O(log n)
        if not nums:
            return -1
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mi = lo + (hi - lo) / 2
            if (nums[mi] < nums[0] and target < nums[0]) \
            or (nums[mi] >= nums[0] and target >= nums[0]):
                if nums[mi] < target:
                    lo = mi + 1
                else:
                    hi = mi
            elif target < nums[mi]:
                lo = mi + 1
            else:
                hi = mi - 1
        return lo if nums[lo] == target else -1

if __name__ == '__main__':
    so = Solution()
    nums = [4,5,6,7,0,1,2]
    # nums = []
    target = 0
    res = so.search(nums, target)
    print res
    
