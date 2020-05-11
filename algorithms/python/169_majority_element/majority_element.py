# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/majority-element

Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
    Input: [3,2,3]
    Output: 3
Example 2:
    Input: [2,2,1,1,1,2,2]
    Output: 2
"""
class Solution(object):

    def majorityElement(self, nums):
        # idea: e.g nums = [x,x,x,y,y,y,x,x]
        # x,x,x counteract y,y,y then left x
        # time: O(n), space: O(1)
        res = None
        cnt = 0
        for x in nums:
            if res != x:
                if cnt:
                    cnt -= 1
                else:
                    res = x
                    cnt = 1
            else:
                cnt += 1
        return res

    def majorityElement_v2(self, nums):
        # idea: using sort, then return the middle item
        # time: O(nlogn), space: O(1)
        nums.sort()
        return nums[len(nums)/2]

    def majorityElement_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea, using an map to count
        # once a cnt more than half, return
        # time: O(n), space: O(n)
        M = {}
        n = len(nums)
        for x in nums:
            M[x] = 1 + M[x] if x in M else 1
            if M[x] > n / 2:
                return x
        return None

if __name__ == "__main__":
    so = Solution()
    nums = [2,2,1,1,1,2,2]
    res = so.majorityElement(nums)
    print res
