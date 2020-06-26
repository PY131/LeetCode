# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        i = 2
        p0 = p1 = 1
        while i <= number:
            p1 = p1 + p0
            p0 = p1 - p0
            i += 1
        return p1