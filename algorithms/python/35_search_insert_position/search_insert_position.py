# coding: utf8
# python 2.7
"""
@author: Pn
@problem_info:    
    Given a sorted array and a target value, 
    return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.
    You may assume no duplicates in the array.

Example 1:
    Input: [1,3,5,6], 5
    Output: 2

Example 2:
    Input: [1,3,5,6], 2
    Output: 1

link: https://leetcode-cn.com/problems/search-insert-position
"""
class Solution(object):

    def searchInsert_v2(self, nums, target):
        '''method 1, binary search - O(logn)
        '''
        n = len(nums)
        if n == 0:
            return 0
        lo = 0
        hi = n - 1
        while lo < hi:
            mi = (lo + hi) / 2
            if nums[mi] < target:
                lo = mi + 1
            else:
                hi = mi
        return lo if target <= nums[lo] else lo + 1

    def searchInsert(self, nums, target):
        '''method 1, brute-force traversal - O(n)
        '''
        i = 0
        while i < len(nums):
            if target <= nums[i]:
                break
            else:
                i += 1
        return i

if __name__ == '__main__':
    s = Solution()
    nums = [1,3,5,6]
    target = 7
    print nums
    print target
    print s.searchInsert_v2(nums, target)    
