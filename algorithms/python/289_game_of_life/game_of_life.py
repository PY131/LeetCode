# coding: utf8
# python 2.7
"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

Link: https://leetcode-cn.com/problems/game-of-life
"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        :complexity: time: O(m*n), space: O(m*n)
        """
        def update_tmp(i, j, m, n, tmp):
            ops = [
                [-1, -1],[-1, 0],[-1, +1],
                [0,  -1],        [0,  +1],
                [+1, -1],[+1, 0],[+1, +1],
            ]
            for op in ops:
                i_tmp = i + op[0]
                j_tmp = j + op[1]
                if i_tmp < 0 or i_tmp > m - 1 or j_tmp < 0 or j_tmp > n - 1:
                    continue
                tmp[i_tmp][j_tmp] += 1

        m = len(board)
        n = len(board[0]) if m else 0
        tmp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    update_tmp(i, j, m, n, tmp)
        for i in range(m):
            for j in range(n):
                if tmp[i][j] < 2 or tmp[i][j] > 3:
                    board[i][j] = 0
                elif tmp[i][j] == 3:
                    board[i][j] = 1
        return board

if __name__ == "__main__":
    so = Solution()
    board = [
        [0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0]
    ]
    res = so.gameOfLife(board)
    print res
