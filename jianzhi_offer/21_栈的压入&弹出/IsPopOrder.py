# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        n = len(pushV)
        i = 0
        s = []
        for x in popV:
            while not s or s[-1] != x:
                if i < n:
                    s.append(pushV[i])
                    i += 1
                else:
                    return False
            s.pop()
        if s:
            return False
        return True