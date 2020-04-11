# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/climbing-stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:
    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step a
    2. 1 step + 2 steps
    3. 2 steps + 1 step
"""

class Solution(object):

    def climbStairs(self, n):
        """on the base of v1, as M[n] only depends on previous two, we can do iteratively by only record two variables
        :complexity: time: O(n) sapce: O(1)
        """
        N_1 = 1
        N_2 = 1
        for _ in range(2, n + 1):
            N_1 = N_1 + N_2
            N_2 = N_1 - N_2
        return N_1

    def climbStairs_v1(self, n):
        """
        :type n: int
        :rtype: int
        :idea: using DP, with a map to record each stair's cost
        :complexity: time: O(n) sapce: O(n)
        """
        M = {}
        M[0] = 1
        M[1] = 1
        for i in range(2, n + 1):
            M[i] = M[i-1] + M[i-2]
        return M[n]

if __name__ == '__main__':
    s = Solution()
    res = s.climbStairs(3)
    print res

    
 