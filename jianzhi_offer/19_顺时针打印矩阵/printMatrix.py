# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        i0 = j0 = 0
        while m - 2 * i0 > 0 and n - 2 * j0 > 0:
            for j in range(j0, n - j0):
                res.append(matrix[i0][j])
                print "-----1-th:", i0, j
            for i in range(i0 + 1, m - 1 - i0):
                res.append(matrix[i][n - 1 - j0])
                print "-----2-th:", i, n - 1 - j0
            if i0 != m - 1 - i0:
                for j in range(n - 1 - j0, j0 - 1, -1):
                    res.append(matrix[m - 1 - i0][j])
                    print "-----3-th:", m - 1 - i0, j
            if j0 != n - 1 - j0:
                for i in range(m - 2 - i0, i0, -1):
                    res.append(matrix[i][j])
                    print "-----4-th:", i, j
            i0 += 1
            j0 += 1
        return res

if __name__ == '__main__':
    so = Solution()
    # mat = [[1, 2],[3, 4]]
    mat = [[1]]
    # mat = [[1], [2], [3], [4]]
    print so.printMatrix(mat)
