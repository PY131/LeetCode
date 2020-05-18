# coding: utf8
# python 2.7
"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:
    Input: [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Link: https://leetcode-cn.com/problems/longest-consecutive-sequence
"""
class Solution(object):

    def longestConsecutive(self, nums):
        # as our target is O(n) in time
        # using a set for O(1) search complexity
        res = 0
        a = set(nums)
        for x in nums:
            if x - 1 not in a:  # new candidate's beginning
                tmp = 0
                while x in nums:
                    tmp += 1
                    x += 1
                if res < tmp:
                    res = tmp
        return res

    def longestConsecutive_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea first, using sort, for O(n log n) in time
        nums = list(set(nums))
        nums.sort()
        res = 0
        tmp = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] - nums[i-1] == 1:
                tmp += 1
            else:
                tmp = 1
            if res < tmp:
                res = tmp
        return res

if __name__ == "__main__":
    so = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    nums = [1,2,0,1]
    res = so.longestConsecutive(nums)
    print res
