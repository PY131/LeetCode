# coding: utf8
# python 2.7
"""
: https://leetcode-cn.com/problems/power-of-three

Given an integer, write a function to determine if it is a power of three.

Example 1:
    Input: 27
    Output: true
Example 2:
    Input: 0
    Output: false
Example 3:
    Input: 9
    Output: true
Example 4:
    Input: 45
    Output: false

Follow up:
Could you do it without using any loop / recursion?
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        :idea: just using a loop to do 3 * 3 * 3...
        :complexity: time: O(log_3^n), space: O(1)
        """
        x = 1
        while x < n:
            x = 3 * x
        return x == n

if __name__ == "__main__":
    so = Solution()
    res = so.isPowerOfThree(0)
    print res
