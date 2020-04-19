# coding: utf8
# python 2.7
"""
: https://leetcode-cn.com/problems/set-matrix-zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
    Input: 
    [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    Output: 
    [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]

Example 2:
    Input: 
    [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    Output: 
    [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]

Follow up:
    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?
"""
class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        :idea: just using the bad idea
        :complexity: time: O(mn), space: O(m+n)
        """
        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    rows.append(i)
                    cols.append(j)
        for i in rows:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
        for j in cols:
            for i in range(len(matrix)):
                matrix[i][j] = 0

if __name__ == '__main__':
    s = Solution()
    mat = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeroes(mat)
    for i in range(len(mat)):
        print mat[i]
