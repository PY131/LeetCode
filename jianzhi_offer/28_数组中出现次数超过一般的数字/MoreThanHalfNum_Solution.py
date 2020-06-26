# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        res = 0
        cnt = 0
        for x in numbers:            
            if cnt == 0 or res == x:
                res = x
                cnt += 1
            else:
                cnt -= 1
        if cnt > 0:
            cnt_2 = 0
            for x in numbers:
                if x == res:
                    cnt_2 += 1
            res = res if cnt_2 > len(numbers) / 2 else 0
        else:
            res = 0
        return res