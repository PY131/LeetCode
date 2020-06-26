# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number < 3:
            return number
        pre = 1
        cur = 2
        i = 3
        while i <= number:
            cur = cur + pre
            pre = cur - pre
            i += 1
        return cur
        