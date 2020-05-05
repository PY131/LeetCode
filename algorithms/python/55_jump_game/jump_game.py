# coding: utf8
# python 2.7
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. 
                 Its maximum jump length is 0, which makes it impossible to reach the last index.

Link: https://leetcode-cn.com/problems/jump-game
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        :using DP, time: O(n), space: O(1)
        """
        n = len(nums)
        max_idx = 0
        for i in range(n):
            if max_idx < i or max_idx > n - 2:
                break
            if max_idx < i + nums[i]:
                max_idx = i + nums[i]
        if max_idx > n - 2:
            return True
        return False

if __name__ == '__main__':
    so = Solution()
    nums = [3,2,1,0,4]
    res = so.canJump(nums)
    print res    
