# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/first-missing-positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
    Input: [1,2,0]
    Output: 3
Example 2:
    Input: [3,4,-1,1]
    Output: 2

Your algorithm should run in O(n) time and uses constant extra space.
"""
class Solution(object):

    def firstMissingPositive(self, nums):
        """in previous one we alloc extra O(n) space, now optimize it
        """
        n = len(nums)
        # ahead, find if 1 is exist
        if 1 not in nums:
            return 1
        # 1-st transfer every unexpected item val not in [1,n] to 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        # 2-nd iterate every expected item val in [1,n], change it's to negetive
        for x in nums:
            nums[abs(x) - 1] = -abs(nums[abs(x) - 1])
        # 3-rd find the first not equal to -1
        for i in range(n):
            if nums[i] < 0:
                continue
            return i + 1
        return n + 1

    def firstMissingPositive_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: if use sort, time complexity of O(n * log n)
        #       how to reduce to O(n)? how about using index to mard
        # the method here using O(n) both in time and space
        n = len(nums)
        tmp = [0] * (n + 1)
        for i in range(n):
            if nums[i] < 0 or nums[i] > n:
                nums[i] = 0
        for x in nums:
            if x:
                tmp[x] = 1
        for i in range(1, n+1):
            if not tmp[i]:
                return i
        return n + 1

if __name__ == "__main__":
    so = Solution()
    nums = [2]
    res = so.firstMissingPositive(nums)
    print res
