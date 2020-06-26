# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        # assert index > 0
        if index < 1:
            return 0
        res = [1]
        i = 0
        p2 = p3 = p5 = 0
        while i < index:
            new = min(res[p2] * 2, res[p3] * 3, res[p5] * 5)
            res.append(new)
            if new == res[p2] * 2:
                p2 += 1
            if new == res[p3] * 3:
                p3 += 1
            if new == res[p5] * 5:
                p5 += 1
            i += 1
            
        return res[index - 1]