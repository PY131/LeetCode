# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/3sum-closest/

- Problems:
    Given an array nums of n integers and an integer target, 
    find three integers in nums such that the sum is closest to target. 
    Return the sum of the three integers. 
    You may assume that each input would have exactly one solution.

- Example:
    Given array nums = [-1, 2, 1, -4], and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        :分析如下: 
            先对nums进行排序
                  nums = [o,  o,  o, ...,  o,  o]
                          |   |                |
                          v   v                v
                  index:  i   j                k
                    num:  x   y                z
            dis = x + y + z - target
            if sum > 0: k--
            elif sum < 0: j++
            record the smallest sum (closest) during iteration
        :复杂度: O(n^2)
        """
        res = None
        min_dis = None
        n = len(nums)
        nums.sort()
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if (not res and res != 0) or abs(s - target) < min_dis:
                    min_dis = abs(s - target)
                    res = s
                if s - target > 0:
                    k -= 1
                elif s - target < 0:
                    j += 1
                else: 
                    return res
        return res

if __name__ == "__main__":
    nums = [0,2,1,-3]
    target = 1
    s = Solution()
    res = s.threeSumClosest(nums, target)
    print res
