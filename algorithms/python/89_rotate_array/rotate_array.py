# coding: utf8
# python 2.7
"""
@Link:
    https://leetcode-cn.com/problems/rotate-array

@Problem:
    Given an array, rotate the array to the right by k steps, where k is non-negative.

@Example #1:

    Input: [1,2,3,4,5,6,7] and k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]
    
@Example #2:

    Input: [-1,-100,3,99] and k = 2
    Output: [3,99,-1,-100]
    Explanation: 
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]

@Note:
    Try to come up as many solutions as you can, 
    there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
"""

class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < k:
            k = k % n
        tmp = nums[-k:]
        for i in range(n - k - 1, -1, -1):
            nums[i+k] = nums[i]
        for i in range(k):
            nums[i] = tmp[i]

    def rotate_v2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < k:
            k = k % n
        if k == 0:
            return
        tmp = nums[-k:]
        nums[k:] = nums[:n-k]
        nums[:k] = tmp

if __name__ == "__main__":
    so = Solution()
    # arr = [1,2,3,4,5,6,7]
    arr = [1]
    print "before: ", arr
    so.rotate_v2(arr, 0)
    print "after:", arr

