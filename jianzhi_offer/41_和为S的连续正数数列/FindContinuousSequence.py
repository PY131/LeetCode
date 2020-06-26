# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        for i in range(1, tsum):
            s = 0
            j = i
            while s < tsum:
                s += j
                j += 1
            if s == tsum:
                res.append([x for x in range(i, j)])
        return res