# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/pascals-triangle/
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

    Input: 5
    Output:
    [
          [1],
         [1,1],
        [1,2,1],
       [1,3,3,1],
      [1,4,6,4,1]
    ]
"""
class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        :iead: 
            [x, x, x] -> [y, y, y, y]
            is
            [x, x, x, 0]
             +  +  +  +
            [0, x, x, x]
             =  =  =  =
            [y, y, y, y]
        """
        if numRows < 1:
            return []
        res = [[1]]
        for i in range(1, numRows):
            row_new = map(lambda x, y: x + y, res[i-1] + [0], [0] + res[i-1])
            res.append(row_new)
        return res

    def generate_v1(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        :complexity: time: O(n^2), space: O(n^2)
        """
        if numRows < 1:
            return []
        res = [[1]]
        for i in range(1, numRows):
            new_row = []
            for j in range(i + 1):
                x = 1
                if 0 < j and j < i:
                    x = res[i-1][j-1] + res[i-1][j]                    
                new_row.append(x)
            res.append(new_row)
        return res

if __name__ == "__main__":
    so = Solution()
    res = so.generate(10)
    for l in res:
        print l
