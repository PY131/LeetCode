# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/single-number-ii

Given a non-empty array of integers, every element appears three times except for one, 
which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
    Input: [2,2,3,2]
    Output: 3

Example 2:
    Input: [0,1,0,1,0,1,99]
    Output: 99
"""

class Solution(object):

    def singleNumber(self, nums):
        """using logic operation
        """
        seen_once = 0  # only changed when seen_twice not changed
        seen_twice = 0  # only changed when seen_once not changed
        for x in nums:
            seen_once = ~seen_twice & (seen_once ^ x)
            seen_twice = ~seen_once & (seen_twice ^ x)
        return seen_once

    def singleNumber_v2(self, nums):
        """
        :on the base of v2, using hashset - X, as 3sum(X) - sum(nums) = 2x, x => only one
        :complexity: time: O(n), space: O(n)
        """
        return (3 * sum(set(nums)) - sum(nums)) / 2

    def singleNumber_v1(self, nums):
        """
        :method: we can use hashmap to record each appear count, then find that appears only once
        :complexity: time: O(n), space: O(n)
        """
        M = {}
        for num in nums:
            if num in M:
                M[num] += 1
            else:
                M[num] = 1
        for num in nums:
            if M[num] == 1:
                return num 
        return None

    def singleNumber_v0(self, nums):
        """
        :method: sort array then iteration
        :complexity: time: O(nlogn), space: O(1)
        """
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i+1]:
                return nums[i]
            i += 3
        return nums[-1]

if __name__ == "__main__":
    so = Solution()
    arr = [2,2,1,2]
    res = so.singleNumber(arr)
    print res
