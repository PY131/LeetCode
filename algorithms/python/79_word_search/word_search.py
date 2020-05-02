# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/word-search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:
    board =
    [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    Given word = "ABCCED", return true.
    Given word = "SEE", return true.
    Given word = "ABCB", return false.
 
Constraints:

    board and word consists only of lowercase and uppercase English letters.
    1 <= board.length <= 200
    1 <= board[i].length <= 200
    1 <= word.length <= 10^3
"""

class Solution(object):

    def exist(self, board, word):
        # using a loop rewrite the dfs search for a better code format
        if not word:
            return True
        m = len(board)
        n = len(board[0]) if m else 0
        used = [[False] * n for i in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j, path, depth):
            if len(word) == depth + 1:
                return ''.join(path) == word
            if path[-1] != word[depth]:
                return False
            for d in directions:
                new_i, new_j = i + d[0], j + d[1]
                if new_i < 0 or new_i > m - 1 or new_j < 0 or new_j > n - 1:
                    continue
                if used[new_i][new_j]:
                    continue
                path.append(board[new_i][new_j])
                used[new_i][new_j] = True
                if dfs(new_i, new_j, path, depth+1):
                    return True
                used[new_i][new_j] = False
                path.pop()
            return False

        for i in range(m):
            for j in range(n):
                used[i][j] = True
                if dfs(i, j, [board[i][j]], 0):
                    return True
                used[i][j] = False
        return False


    def exist_v1(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        m = len(board)
        n = len(board[0]) if m else 0
        used = [[False] * n for i in range(m)]

        def dfs(i, j, path, depth):
            # search end
            if len(word) == depth + 1:
                return ''.join(path) == word
            # cut branch
            if path[-1] != word[depth]:
                return False
            # dfs
            if i > 0 and not used[i-1][j]:
                path.append(board[i-1][j])
                used[i-1][j] = True
                if dfs(i-1, j, path, depth+1):
                    return True
                used[i-1][j] = False
                path.pop()
            if i < m-1 and not used[i+1][j]:
                path.append(board[i+1][j])
                used[i+1][j] = True
                if dfs(i+1, j, path, depth+1):
                    return True
                used[i+1][j] = False
                path.pop()
            if j > 0 and not used[i][j-1]:
                path.append(board[i][j-1])
                used[i][j-1] = True
                if dfs(i, j-1, path, depth+1):
                    return True
                used[i][j-1] = False
                path.pop()
            if j < n-1 and not used[i][j+1]:
                path.append(board[i][j+1])
                used[i][j+1] = True
                if dfs(i, j+1, path, depth+1):
                    return True
                used[i][j+1] = False
                path.pop()
            # default
            return False

        for i in range(m):
            for j in range(n):
                used[i][j] = True
                if dfs(i, j, [board[i][j]], 0):
                    return True
                used[i][j] = False
        return False

if __name__ == '__main__':
    so = Solution()
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word = "ABCCED"
    res = so.exist(board, word)
    print res
