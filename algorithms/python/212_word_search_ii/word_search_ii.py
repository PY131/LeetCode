# coding: utf8
# python 2.7

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m = len(board)
        n = len(board[0]) if m else 0
        res = set()
        words = set(words)
        words_axu = set([''])
        for w in words:
            tmp = ''
            for i in range(len(w)):
                tmp += w[i]
                words_axu.add(tmp)

        dirs = [(0, 1),(1, 0),(0, -1),(-1, 0)]
        mask = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j, path):
            if i < 0 or i >= m or j < 0 or j >= n \
            or mask[i][j] \
            or path not in words_axu:
                return

            path += board[i][j]
            mask[i][j] = True
            if path in words:
                res.add(path)
            for di, dj in dirs:
                dfs(i+di, j+dj, path)
            path = path[:-1]
            mask[i][j] = False

        for i in range(m):
            for j in range(n):
                dfs(i, j, '')

        return list(res)

if __name__ == "__main__":
    so = Solution()
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    res = so.findWords(board, words)
    print res
