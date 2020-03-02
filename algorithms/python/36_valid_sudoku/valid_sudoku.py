# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/valid-sudoku

@author: Pn

Determine if a 9x9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, 
where empty cells are filled with the character '.'.

Example 1:

    Input:
    [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    Output: true

Example 2:

    Input:
    [
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    Output: false

Explanation: 
    Same as Example 1, except with the 5 in the top left corner being modified to 8. 
    Since there are two 8's in the top left 3x3 sub-box, it is invalid.

"""
class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        set_col = [set() for i in range(9)]
        set_row = [set() for i in range(9)]
        for sqr in range(9):
            set_a = set()
            for i in range(3):
                for j in range(3):
                    row = (sqr / 3 * 3) + i
                    col = (sqr % 3 * 3) + j
                    num = board[row][col]
                    if num == '.':
                        continue
                    if num in set_a \
                    or num in set_row[row] \
                    or num in set_col[col]:
                        return False
                    set_a.add(num)
                    set_row[row].add(num)
                    set_col[col].add(num)
        return True

if __name__ == '__main__':
    so = Solution()
    board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    res = so.isValidSudoku(board)
    print res    
