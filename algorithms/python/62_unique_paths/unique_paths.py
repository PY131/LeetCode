# coding: utf8
# python 2.7
"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Example:
    Input: m = 3, n = 2
    Output: 3
    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Right -> Down
    2. Right -> Down -> Right
    3. Down -> Right -> Right

Link: https://leetcode-cn.com/problems/unique-paths
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # using DP, time: O(m*n), space: O(m*n)
        S = [[0] * n for _ in range(m)]
        S[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i > 0:
                    S[i][j] += S[i-1][j]
                if j > 0:
                    S[i][j] += S[i][j-1]
        return S[m-1][n-1]

if __name__ == '__main__':
    so = Solution()
    m, n = 3, 2
    res = so.uniquePaths(m, n)
    print res
