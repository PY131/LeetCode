# coding: utf8
# python 2.7
"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.

Example 1:
    Input: [1,3,4,2,2]
    Output: 2
Example 2:
    Input: [3,1,3,4,2]
    Output: 3

Note:
    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.

Link: https://leetcode-cn.com/problems/find-the-duplicate-number
"""

class Solution(object):

    def findDuplicate(self, nums):
        '''using floyd pointer method, cost O(1) in time
        '''
        p0 = p1 = p2 = nums[0]
        while True:
            p0 = nums[nums[p0]]
            p1 = nums[p1]
            if p0 == p1:
                break
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1

    def findDuplicate_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :using a set to record, then iterate until repeat one found 
        :complexity O(n) in time and the same in space
        """
        s = set()
        for x in nums:
            if x in s:
                return x
            s.add(x)
        return -1

if __name__ == "__main__":
    so = Solution()
    nums = [3,2,1,5,4,7,6,3]
    res = so.findDuplicate(nums)
    print res
