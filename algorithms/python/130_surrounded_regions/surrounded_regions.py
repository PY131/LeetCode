# coding: utf8
# python 2.7
"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Link: https://leetcode-cn.com/problems/surrounded-regions
"""
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0]) if m > 0 else 0
        mask = [[False for _ in range(n)] for _ in range(m)]
        directions = [
            (-1, 0),(0, 1),(1, 0),(0, -1)
        ]
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O' or mask[i][j] == True:
                return
            board[i][j] = '-1'
            mask[i][j] == True
            for di, dj in directions:
                dfs(i+di, j+dj)

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == 'O':
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '-1':
                    board[i][j] = 'O'

if __name__ == "__main__":
    so = Solution()
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X'],
    ]
    so.solve(board)
    for row in board:
        print row
