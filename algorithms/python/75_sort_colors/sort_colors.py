# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/sort-colors

Given an array with n objects colored red, white or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.

Example:
    Input: [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        :idea, using two pointer for swap 0 or 2
        :complexity: time: O(n) space O(1)
        """
        n = len(nums)
        i = p0 = 0
        p2 = n - 1
        while i <= p2:
            if nums[i] == 2:
                nums[p2], nums[i] = nums[i], nums[p2]
                p2 -= 1
            elif nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1
                i += 1
            else:
                i += 1

if __name__ == '__main__':
    so = Solution()
    nums = [2,0,2,1,1,0]
    so.sortColors(nums)
    print nums
