# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        res = []
        tmp = float('+inf')
        M = {}
        for x in array:
            if x in M:
                M[x] += 1
            else:
                M[x] = 1
        for x in array:
            y = tsum - x
            if y < x:
                continue
            cnt = M.get(y, 0)
            if x < y and (x == y and cnt > 1) or (x != y and cnt > 0):
                if x * y < tmp:
                    tmp = x * y
                    res = [x, y]
        return res