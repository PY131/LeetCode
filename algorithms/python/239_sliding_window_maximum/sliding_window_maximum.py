# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/sliding-window-maximum

Given an array nums, 
there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. 
Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation:
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        :implement of a max filter
        :time cost of O(n)
        """
        res = []
        win = []
        n = len(nums)
        for i in range(n):
            while win and win[-1] < nums[i]:
                win.pop()
            if win and i - k >= 0 and win[0] == nums[i - k]:
                win.pop(0)
            win.append(nums[i])
            if i > k - 2:
                res.append(win[0])
        return res       

# test code
if __name__ == '__main__':
    so = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    res = so.maxSlidingWindow(nums, k)
    print res
