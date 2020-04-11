# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/maximum-subarray
Given an integer array nums, 
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
    If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution(object):

    def maxSubArray(self, nums):
        """
        :idea: using DP
            e.g. max_current_sum[i] = max_current_sum[i-1] + val if max_current_sum[i-1]>0 else val
        :complexity: time: O(n) space: O(1)
        """
        dp = nums[0]
        res = dp
        for x in nums[1:]:
            dp = max([x, dp + x])
            if res < dp:
                res = dp
        return res

    def maxSubArray_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :idea: using greedy strategy
        :complexity: time: O(n) space: O(n)
        """
        max_current_sum = [nums[0]]
        for val in nums[1:]:
            max_current_sum.append(
                max_current_sum[-1] + val if max_current_sum[-1] > 0 else val
            )
        return max(max_current_sum)

if __name__ == '__main__':
    S = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = S.maxSubArray(nums)
    print res
