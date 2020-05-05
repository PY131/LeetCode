# coding: utf8
# python 2.7
"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
    Input: [10,9,2,5,3,7,101,18]
    Output: 4 
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:
    There may be more than one LIS combination, it is only necessary for you to return the length.
    Your algorithm should run in O(n2) complexity.
    Follow up: Could you improve it to O(n log n) time complexity?

Link: https://leetcode-cn.com/problems/longest-increasing-subsequence
"""

class Solution(object):

    def lengthOfLIS(self, nums):
        """
        try to optimize the time complexity to O(n log n), log n -> we need bi-search in a sorted array
        """
        if not nums:
            return 0
        n = len(nums)
        d = [0] * (n + 1) 
        p = 1
        d[p] = nums[0]
        for x in nums:
            if x > d[p]:
                p += 1
                d[p] = x
            else:
                l = 0
                h = p
                while l < h:
                    m = l + ((h - l) >> 1)
                    if d[m] < x:
                        l = m + 1
                    else:
                        h = m
                d[l] = x
        return p

    def lengthOfLIS_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: using DP, time: O(n^2), space: O(n)
        if not nums:
            return 0
        n = len(nums)
        S = [0] * n
        res = 0
        for i in range(n):
            tmp = 0
            for j in range(i):
                if nums[j] < nums[i] and tmp < S[j]:
                    tmp = S[j]
            S[i] = tmp + 1
            if res < S[i]:
                res = S[i]
        return res

if __name__ == '__main__':
    so = Solution()
    nums = [10,9,2,5,3,7,101,18]
    res = so.lengthOfLIS(nums)
    print res
