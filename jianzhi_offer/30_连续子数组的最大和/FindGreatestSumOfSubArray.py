# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        res = array[0]
        s = array[0]
        for x in array[1:]:
            if s > 0:
                s = s + x
            else:
                s = x
            if s > res:
                res = s
        return res