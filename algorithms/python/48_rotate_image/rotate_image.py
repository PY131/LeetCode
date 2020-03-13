# coding: utf8
# python 2.7
"""
@author: Pn

@link: https://leetcode-cn.com/problems/rotate-image/

@Problem_info: 
    You are given an n x n 2D matrix representing an image.
    Rotate the image by 90 degrees (clockwise).

@Note:
    You have to rotate the image in-place, 
    which means you have to modify the input 2D matrix directly. 
    DO NOT allocate another 2D matrix and do the rotation.

@example:
    Given input matrix = 
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],

    rotate the input matrix in-place such that it becomes:
    [
        [7,4,1],
        [8,5,2],
        [9,6,3]
    ]
"""

class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        :idea:
            - get the next point location (i,j) = (j,n-1-i)
            - each item in one quadrant can trigger all four quadrant items' rotation, 
            - such as:
                (i, j) --------->  (j, n-1-i)
                   ^                    |
                   |                    v
                (n-1-j, i) <----- (n-1-i, n-1-j)
        :complexity: time: O(n^2), space: O(1)
        """
        N = len(matrix)
        for i in range(N/2):
            for j in range(N - N/2):
                cnt = 0
                tmp = matrix[i][j]
                while cnt < 4:
                    i, j = j, N - 1 - i
                    tmp_new = matrix[i][j]
                    matrix[i][j] = tmp
                    tmp = tmp_new
                    cnt += 1

if __name__ == '__main__':
    S = Solution()
    nums = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    S.rotate(nums)
    print nums
