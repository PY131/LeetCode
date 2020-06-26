# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        self.res = 0
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]
        mask = [[0 for i in range(cols)] for j in range(rows)]
        
        def check(i, j, th):
            s = 0
            for x in [i, j]:
                while x:
                    s += x % 10
                    x = x / 10
            if s > th:
                return False
            return True
        
        def dfs(i, j, m, n, th):
            # 判断当前结点是否已经被访问
            if i < 0 or i >= m or j < 0 or j >= n or mask[i][j] == 1:
                return
            # 判断是否属于能进入的结点
            if not check(i, j, th):
                return
            # +1
            self.res += 1
            mask[i][j] = 1
            # 继续深度搜索 -> 上下左右
            for di, dj in directions:
                dfs(i + di, j + dj, m, n, th)
            
        dfs(0, 0, rows, cols, threshold)
        return self.res

if __name__ == '__main__':
    so = Solution()
    res = so.movingCount(2, 3, 2)
    print res
