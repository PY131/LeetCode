# coding: utf8
# python 2.7
"""
@author: Pn

@link: https://leetcode-cn.com/problems/move-zeroes

@problem_info: 
    Given an array nums, write a function to move all 0's to the end of it 
    while maintaining the relative order of the non-zero elements.

@example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

@note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""

class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        :complexity: time: O(n), space: O(1)
        """
        idx = 0
        for x in nums:
            if x != 0:
                nums[idx] = x
                idx += 1
        for i in range(idx, len(nums)):
            nums[i] = 0

if __name__ == '__main__':
    S = Solution()
    nums = [0,1,0,3,12]
    S.moveZeroes(nums)
    print nums
