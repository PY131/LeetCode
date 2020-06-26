# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        directions = [
            (-1, 0),
            (0,  1),
            (1,  0),
            (0, -1)
        ]
        mask = [[False for _ in range(cols)] for _ in range(rows)]
        
        def dfs(i, j, depth):
            # 判断是否能走到当前结点
            if i < 0 or i >= rows or j < 0 or j >= cols \
            or mask[i][j] == True \
            or matrix[i][j] != path[depth]:
                return False
            # 是否已命中
            if depth == len(path) - 1:
                return True
            # 继续搜索
            mask[i][j] = True
            for di, dj in directions:
                if dfs(i + di, j + dj, depth+1):
                    return True
            # 回溯
            mask[i][j] = False
            return False
            
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False

if __name__ == '__main__':
    so = Solution()
    mat = [
        ['a', 'b', 'c', 'e'],
        ['s', 'f', 'c', 's'],
        ['a', 'd', 'e', 'e'],
    ]
    path = 'abcced'
    res = so.hasPath(mat, len(mat), len(mat[0]), path)
    print res
