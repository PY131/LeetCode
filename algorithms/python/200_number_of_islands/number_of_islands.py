# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/number-of-islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
    Input:
        11110
        11010
        11000
        00000
    Output: 1

Example 2:
    Input:
        11000
        11000
        00100
        00011
    Output: 3
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # idea: using DFS
        # complexity: time O(n) space O(1) while n is the area of grid
        res = 0
        M = len(grid)
        N = len(grid[0]) if M else 0

        def dfs(g, i, j, m, n):
            g[i][j] = '0'
            if i > 0 and g[i-1][j] == '1':
                dfs(g, i-1, j, m, n)
            if j > 0 and g[i][j-1] == '1':
                dfs(g, i, j-1, m, n)
            if i < m-1 and g[i+1][j] == '1':
                dfs(g, i+1, j, m, n)
            if j < n-1 and g[i][j+1] == '1':
                dfs(g, i, j+1, m, n)

        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    res += 1
                    dfs(grid, i, j, M, N)
        return res

if __name__ == '__main__':
    S = Solution()
    grid = [
        ['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','1'],
    ]
    res = S.numIslands(grid)
    print res
